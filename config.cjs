const fs=require('node:fs/promises');const path=require('node:path');
const AGREEMENT_VERSION='2026-10-29.1';
const defaults={language:'zh',mode:'local',preference:'auto',downloadSource:'auto',customModelUrl:'',activeProvider:'seedream',apis:{},agreement:null};
class ConfigStore{
 constructor(folder,safeStorage){this.file=path.join(folder,'preferences-v3.json');this.secure=path.join(folder,'credentials-v3.bin');this.safeStorage=safeStorage;this.values=structuredClone(defaults);this.keys={};this.chain=Promise.resolve();}
 async load(){try{this.values={...structuredClone(defaults),...JSON.parse(await fs.readFile(this.file,'utf8'))};}catch{}try{this.keys=JSON.parse(this.safeStorage.decryptString(await fs.readFile(this.secure)));}catch{}return this.snapshot();}
 accepted(){return this.values.agreement?.version===AGREEMENT_VERSION;}
 snapshot(){return structuredClone({...this.values,apis:Object.fromEntries(Object.entries(this.values.apis).map(([k,v])=>[k,{...v,hasKey:!!this.keys[k]}])),hasHfToken:!!this.keys.huggingfaceDownload,agreementVersion:AGREEMENT_VERSION,accepted:this.accepted()});}
 api(){const v=this.values.apis[this.values.activeProvider];return v?structuredClone({...v,key:this.keys[this.values.activeProvider]||''}):null;}
 update(input){const v=structuredClone(input);const operation=this.chain.catch(()=>{}).then(()=>this.apply(v));this.chain=operation;return operation;}
 async apply(v){const next=structuredClone(this.values),keys=structuredClone(this.keys);
 for(const [field,allowed,error] of [['language',['zh','en'],'INVALID_LANGUAGE'],['mode',['local','api'],'INVALID_MODE'],['preference',['auto','compact','quality','custom'],'INVALID_PREFERENCE'],['downloadSource',['auto','official','mirror'],'INVALID_SOURCE']])if(v[field]!==undefined){if(!allowed.includes(v[field]))throw Error(error);next[field]=v[field];}
 if(v.customModelUrl!==undefined)next.customModelUrl=String(v.customModelUrl).slice(0,2000);
 if(v.hfToken!==undefined&&v.hfToken!=='')keys.huggingfaceDownload=String(v.hfToken).trim();if(v.clearHfToken)delete keys.huggingfaceDownload;
 if(v.acceptAgreement===AGREEMENT_VERSION)next.agreement={version:AGREEMENT_VERSION,acceptedAt:new Date().toISOString()};if(v.license9b!==undefined)next.license9b=v.license9b===true;
 if(v.api){const {validateConfig}=await import('./app/lib/providers.mjs').catch(()=>import(require('node:url').pathToFileURL(path.join(process.resourcesPath,'app/lib/providers.mjs')).href));const a=validateConfig(v.api),previous=next.apis[a.provider];
 if(keys[a.provider]&&previous?.endpoint!==a.endpoint&&!a.key&&!v.api.clearKey)throw Error('KEY_REENTRY_REQUIRED');
 if(a.key)keys[a.provider]=a.key;if(v.api.clearKey)delete keys[a.provider];delete a.key;next.apis[a.provider]=a;next.activeProvider=a.provider;}
 const hasKeys=Object.keys(keys).length>0;if(hasKeys&&!this.safeStorage.isEncryptionAvailable())throw Error('SECURE_STORAGE_UNAVAILABLE');
 const encrypted=hasKeys?this.safeStorage.encryptString(JSON.stringify(keys)):null;await fs.mkdir(path.dirname(this.file),{recursive:true});
 await fs.writeFile(this.file+'.tmp',JSON.stringify(next,null,2));if(encrypted)await fs.writeFile(this.secure+'.tmp',encrypted);
 if(encrypted)await fs.rename(this.secure+'.tmp',this.secure);else await fs.rm(this.secure,{force:true});await fs.rename(this.file+'.tmp',this.file);
 this.values=next;this.keys=keys;return this.snapshot();}
}
module.exports={ConfigStore,AGREEMENT_VERSION};
