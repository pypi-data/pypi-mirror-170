const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { ar as union, am as object, ao as string, an as optional, av as enums, ap as boolean } from './auth-dev.js';
import { a as actionConfigStruct } from './action-struct-dev.js';

const TIMESTAMP_RENDERING_FORMATS=["relative","total","date","time","datetime"];

const entitiesConfigStruct=union([object({entity:string(),name:optional(string()),icon:optional(string()),image:optional(string()),secondary_info:optional(string()),format:optional(enums(TIMESTAMP_RENDERING_FORMATS)),state_color:optional(boolean()),tap_action:optional(actionConfigStruct),hold_action:optional(actionConfigStruct),double_tap_action:optional(actionConfigStruct)}),string()]);

export { TIMESTAMP_RENDERING_FORMATS as T, entitiesConfigStruct as e };
