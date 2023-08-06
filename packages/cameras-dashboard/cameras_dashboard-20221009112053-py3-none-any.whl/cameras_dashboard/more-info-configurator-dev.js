const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, $, r, n } from './main-dev.js';
import './stop_propagation-dev.js';
import './ha-circular-progress-dev.js';
import './ha-markdown-dev.js';

let MoreInfoConfigurator=_decorate([n("more-info-configurator")],function(_initialize,_LitElement){class MoreInfoConfigurator extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoConfigurator,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"field",decorators:[t()],key:"_isConfiguring",value(){return false;}},{kind:"field",key:"_fieldInput",value(){return {};}},{kind:"method",key:"render",value:function render(){var _this$stateObj;if(((_this$stateObj=this.stateObj)===null||_this$stateObj===void 0?void 0:_this$stateObj.state)!=="configure"){return $``;}return $`
      <div class="container">
        <ha-markdown
          breaks
          .content=${this.stateObj.attributes.description}
        ></ha-markdown>

        ${this.stateObj.attributes.errors?$`<ha-alert alert-type="error">
              ${this.stateObj.attributes.errors}
            </ha-alert>`:""}
        ${this.stateObj.attributes.fields.map(field=>$`<ha-textfield
            .label=${field.name}
            .name=${field.id}
            .type=${field.type}
            @change=${this._fieldChanged}
          ></ha-textfield>`)}
        ${this.stateObj.attributes.submit_caption?$`<p class="submit">
              <mwc-button
                raised
                .disabled=${this._isConfiguring}
                @click=${this._submitClicked}
              >
                ${this._isConfiguring?$`<ha-circular-progress
                      active
                      alt="Configuring"
                    ></ha-circular-progress>`:""}
                ${this.stateObj.attributes.submit_caption}
              </mwc-button>
            </p>`:""}
      </div>
    `;}},{kind:"method",key:"_fieldChanged",value:function _fieldChanged(ev){const el=ev.target;this._fieldInput[el.name]=el.value;}},{kind:"method",key:"_submitClicked",value:function _submitClicked(){const data={configure_id:this.stateObj.attributes.configure_id,fields:this._fieldInput};this._isConfiguring=true;this.hass.callService("configurator","configure",data).then(()=>{this._isConfiguring=false;},()=>{this._isConfiguring=false;});}},{kind:"field",static:true,key:"styles",value(){return r`
    .container {
      display: flex;
      flex-direction: column;
    }
    p {
      margin: 8px 0;
    }

    a {
      color: var(--accent-color);
    }

    p > img {
      max-width: 100%;
    }

    p.center {
      text-align: center;
    }

    p.submit {
      text-align: center;
      height: 41px;
    }

    ha-circular-progress {
      width: 14px;
      height: 14px;
      margin-right: 20px;
    }
  `;}}]};},s);

export { MoreInfoConfigurator };
