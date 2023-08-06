const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { aE as refine, ao as string } from './auth-dev.js';

const isEntityId=value=>value.includes(".");const entityId=()=>refine(string(),"entity ID (domain.entity)",isEntityId);const isEntityIdOrAll=value=>{if(value==="all"){return true;}return isEntityId(value);};const entityIdOrAll=()=>refine(string(),"entity ID (domain.entity or all)",isEntityIdOrAll);

export { entityId as a, entityIdOrAll as e };
