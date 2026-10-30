def build_prompt(cfg, captions):
 pose=cfg.get('action') or captions.get(cfg['poseName'],cfg['poseName'])
 view={'正面':'front view','斜侧':'three-quarter view','侧面':'side profile view','俯视':'high-angle view from above','仰视':'low-angle view from below'}.get(cfg.get('angle'),'')
 paired=cfg.get('personCount')==2 or '双人' in cfg.get('system','')
 if paired:
  if not cfg.get('sourceB'):raise ValueError('A two-person pose requires a second identity reference.')
  prompt=('Create one realistic photograph with exactly TWO fully clothed people. Image 1 supplies ONLY person A identity and clothing. Image 2 supplies ONLY person B identity and clothing. Image 3 supplies ONLY the two-person body pose and camera angle. '
   'Person A and person B perform this action: '+pose+'. Camera: '+view+'. '
   'Preserve person A face, facial features, hairstyle, hair color, skin tone, body type and entire exact outfit from image 1. Preserve person B face, facial features, hairstyle, hair color, skin tone, body type and entire exact outfit from image 2. '
   'Keep each identity and outfit assigned to its own body. Do not blend faces, swap clothing, invent a third person, or copy mannequin skin or anatomy from image 3. Preserve all clothing and accessories. Match the interacting arms, hands, torsos and legs of the pose in image 3. ')
  prompt+=('The user explicitly requests the SAME person playing both roles: create two instances of the person while keeping two separate bodies. ' if cfg.get('samePerson') else 'These are two DISTINCT individuals. Never duplicate person A as person B. Both supplied people must be recognizable. ')
 else:
  prompt=('Edit image 1: change the body pose of the person to this target pose: '+pose+'. Camera: '+view+'. '
   'The target pose and camera framing are shown in image 2. Closely match the positions of the arms, hands, torso, hips and legs in image 2. '
   'Preserve the same recognizable person, facial features, hairstyle, hair color, body shape, skin tone and exact clothing from image 1. Keep all original clothing and accessories fully intact. '
   'Image 2 is ONLY a pose reference. Do not copy its mannequin appearance, face or outfit. The person must visibly perform this action: '+pose+'. ')
 prompt+='Output one coherent, natural photograph. Keep the background and lighting from image 1 when possible. No text, no collage, no reference panels. '
 if cfg.get('note'):prompt+='Additional user instructions: '+cfg['note']
 return prompt
