const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { am as object, ao as string, an as optional, as as array, ax as number, ar as union } from './auth-dev.js';
import { a as actionConfigStruct } from './action-struct-dev.js';
import { e as entitiesConfigStruct } from './entities-struct-dev.js';

const pictureHeaderFooterConfigStruct=object({type:string(),image:string(),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct),double_tap_action:optional(actionConfigStruct)});const buttonsHeaderFooterConfigStruct=object({type:string(),entities:array(entitiesConfigStruct)});const graphHeaderFooterConfigStruct=object({type:string(),entity:string(),detail:optional(number()),hours_to_show:optional(number())});const headerFooterConfigStructs=union([pictureHeaderFooterConfigStruct,buttonsHeaderFooterConfigStruct,graphHeaderFooterConfigStruct]);

export { graphHeaderFooterConfigStruct as g, headerFooterConfigStructs as h };
