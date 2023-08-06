const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { e, i, N as _defineProperty, J as t, O as b } from './main-dev.js';

const dynamicElement=e(class extends i{constructor(partInfo){super(partInfo);_defineProperty(this,"_element",void 0);if(partInfo.type!==t.CHILD){throw new Error("dynamicElementDirective can only be used in content bindings");}}update(_part,[tag,properties]){if(this._element&&this._element.localName===tag){if(properties){Object.entries(properties).forEach(([key,value])=>{this._element[key]=value;});}return b;}return this.render(tag,properties);}render(tag,properties){this._element=document.createElement(tag);if(properties){Object.entries(properties).forEach(([key,value])=>{this._element[key]=value;});}return this._element;}});

export { dynamicElement as d };
