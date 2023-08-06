const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, $, j as _get, k as _getPrototypeOf, f as fireEvent, n } from './main-dev.js';
import { al as assign, am as object, as as array, aw as any, an as optional, ao as string, ap as boolean, aq as assert } from './auth-dev.js';
import { b as baseLovelaceCardConfig } from './base-card-struct-dev.js';
import { HuiStackCardEditor } from './hui-stack-card-editor-dev.js';
import './stop_propagation-dev.js';
import './ha-more-info-dialog-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';
import './hui-card-picker-dev.js';
import './hui-element-editor-dev.js';
import './js-yaml-dev.js';
import './ha-code-editor-dev.js';
import './ha-form-dev.js';
import './dynamic-element-directive-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';
import './entities-struct-dev.js';
import './action-struct-dev.js';
import './config-elements-style-dev.js';

const cardConfigStruct=assign(baseLovelaceCardConfig,object({cards:array(any()),title:optional(string()),square:optional(boolean()),columns:optional(string())}));let HuiGridCardEditor=_decorate([n("hui-grid-card-editor")],function(_initialize,_HuiStackCardEditor){class HuiGridCardEditor extends _HuiStackCardEditor{constructor(...args){super(...args);_initialize(this);}}return {F:HuiGridCardEditor,d:[{kind:"method",key:"setConfig",value:function setConfig(config){assert(config,cardConfigStruct);this._config=config;}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this._config){return $``;}const SCHEMA=[{type:"grid",name:"",schema:[{name:"columns",selector:{select:{options:[{value:"1",label:this.hass.localize(`ui.panel.lovelace.editor.card.grid.big`)},{value:"2",label:this.hass.localize(`ui.panel.lovelace.editor.card.grid.medium`)},{value:"3",label:this.hass.localize(`ui.panel.lovelace.editor.card.grid.small`)}]}}},{name:"title",selector:{text:{}}}// { name: "square", selector: { boolean: {} } },
]}];const data={title:"",square:true,columns:"3",...this._config};return $`
      <div class="formContainer" style="width:90%;margin-left:5%">
        <ha-form
          .hass=${this.hass}
          .data=${data}
          .schema=${SCHEMA}
          .computeLabel=${this._computeLabelCallback}
          @value-changed=${this._valueChanged}
        ></ha-form>
      </div>
      ${_get(_getPrototypeOf(HuiGridCardEditor.prototype),"render",this).call(this)}
    `;}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){fireEvent(this,"config-changed",{config:ev.detail.value});}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>this.hass.localize(`ui.panel.lovelace.editor.card.grid.${schema.name}`);}}]};},HuiStackCardEditor);

export { HuiGridCardEditor };
