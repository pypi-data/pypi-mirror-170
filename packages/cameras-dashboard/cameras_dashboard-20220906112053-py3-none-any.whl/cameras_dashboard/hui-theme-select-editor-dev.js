const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, $, r, f as fireEvent, n } from './main-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';

_decorate([n("hui-theme-select-editor")],function(_initialize,_LitElement){class HuiThemeSelectEditor extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiThemeSelectEditor,d:[{kind:"field",decorators:[e()],key:"value",value:void 0},{kind:"field",decorators:[e()],key:"label",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"method",key:"render",value:function render(){return $`
      <ha-select
        .label=${this.label||`${this.hass.localize("ui.panel.lovelace.editor.card.generic.theme")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})`}
        .value=${this.value}
        @selected=${this._changed}
        @closed=${stopPropagation}
        fixedMenuPosition
        naturalMenuWidth
      >
        <mwc-list-item value="remove"
          >${this.hass.localize("ui.panel.lovelace.editor.card.generic.no_theme")}</mwc-list-item
        >
        ${Object.keys(this.hass.themes.themes).sort().map(theme=>$`<mwc-list-item .value=${theme}>${theme}</mwc-list-item>`)}
      </ha-select>
    `;}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-select {
        width: 100%;
      }
    `;}},{kind:"method",key:"_changed",value:function _changed(ev){if(!this.hass||ev.target.value===""){return;}this.value=ev.target.value==="remove"?undefined:ev.target.value;fireEvent(this,"value-changed",{value:this.value});}}]};},s);
