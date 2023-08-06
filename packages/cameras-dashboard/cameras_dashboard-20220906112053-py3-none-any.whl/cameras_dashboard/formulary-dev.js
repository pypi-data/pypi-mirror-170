const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, dL as getCameraEntities, f as fireEvent, $, z as o, at as mdiClose, X as mdiChevronLeft, dE as localize, dS as sendCameraInformation, dT as sendCameraBrandInformation, r, n } from './main-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-header-bar-dev.js';
import './ha-form-dev.js';
import './ha-checkbox-dev.js';
import './camera-model-icon-button-dev.js';
import './search-input-round-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-check-list-item-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-base-time-input-dev.js';

let HuiCreateDialogCameraFormulary=_decorate([n("raceland-formulary")],function(_initialize,_LitElement){class HuiCreateDialogCameraFormulary extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiCreateDialogCameraFormulary,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"dialogOpen",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"data",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"cameraModelInfo",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"backEvent",value:void 0},{kind:"field",decorators:[e({type:String})],key:"formType",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"registeredCameras",value:void 0},{kind:"field",decorators:[t()],key:"_currTabIndex",value(){return 0;}},{kind:"field",decorators:[t()],key:"validIssue",value:void 0},{kind:"method",key:"showDialog",value:function showDialog(params){this.schema=params.schema;this.backEvent=params.backEvent;this.data=params.data;this.formType=params.formType;this.cameraModelInfo=params.cameraModelInfo;this.dialogOpen=true;this.registeredCameras=getCameraEntities(this.hass.states).map(camera=>camera.name);}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._currTabIndex=0;this.dialogOpen=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});return true;}},{kind:"method",key:"render",value:function render(){if(!this.dialogOpen){return $``;}const schemaBody=this.schema.body;const schemaExtraOptions=this.schema.extra_options;return $`
      <ha-dialog
        open
        scrimClickAction
        hideActions
        @closed=${this.closeDialog}
        class=${o({table:this._currTabIndex===1})}
      >
        <div class="cancel">
          <ha-svg-icon
            dialogAction="close"
            class="cancel-icon"
            slot="icon"
            .path=${mdiClose}
          ></ha-svg-icon>
        </div>
        <div class="header-text">${this.schema.header.title}</div>
        ${this.validIssue?$` <div class="form-issue">${this.validIssue}</div>`:$``}
        <div class="form">
          <ha-form
            .hass=${this.hass}
            .data=${this.data}
            .schema=${schemaBody}
            .computeLabel=${this._computeLabelCallback}
            @value-changed=${this._valueChanged}
          ></ha-form>
          ${schemaExtraOptions&&this.data.advanced_options?$` <ha-form
                .hass=${this.hass}
                .data=${this.data}
                .schema=${schemaExtraOptions}
                .computeLabel=${this._computeLabelCallback}
                @value-changed=${this._valueChanged}
              ></ha-form>`:$``}
        </div>
        <div class="options">
          <mwc-button class="button-confirm" @click=${this._accept}
            >${this.schema.footer.accept}</mwc-button
          >
          ${this.backEvent?$`<mwc-button class="button-back" dialogAction="close" @click=${this._goBack}
                >${this.schema.footer.back}
                <ha-svg-icon class="icon-back" slot="icon" .path=${mdiChevronLeft}></ha-svg-icon
              ></mwc-button>`:$``}
        </div>
      </ha-dialog>
    `;}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{return localize(`form.${schema.name}`);};}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;this.data={...this.data,...config};}},{kind:"method",key:"validInputCustom",value:function validInputCustom(){if(!this.data.name){this.validIssue=localize("form.issues.name");return false;}if(this.registeredCameras.includes(this.data.name)){this.validIssue=localize("form.issues.duplicated_camera_name");return false;}if(!this.data.still_image_url&&!this.data.stream_source){this.validIssue=localize("form.issues.static_stream_source_missing");return false;}return true;}},{kind:"method",key:"validInput",value:function validInput(){if(!this.data.ip){this.validIssue=localize("form.issues.ip_missing");return false;}if(isNaN(Number(this.data.channel))||this.data.channel!==undefined&&this.data.channel<=0){this.validIssue=localize("form.issues.n_cameras");return false;}let cameraNames=[];const channel=parseInt(this.data.channel);if(this.data.channel!==undefined&&channel>1){cameraNames=Array.from({length:channel},(_,k)=>`${this.data.name} ${k+1}`);}else {cameraNames=[this.data.name];}if(cameraNames.filter(value=>this.registeredCameras.includes(value)).length>0){this.validIssue=localize("form.issues.duplicated_camera_name");return false;}return true;}},{kind:"method",key:"_accept",value:async function _accept(){if(this.formType==="custom_camera"){const valid=this.validInputCustom();if(valid===true){const result=await sendCameraInformation(this.hass,this.data);if(result===true){this.closeDialog();fireEvent(this,"update-camera-dashboard");}}}else if(this.formType==="brand_camera"){const valid=this.validInput();if(valid===true){await sendCameraBrandInformation(this.hass,this.data);this.closeDialog();fireEvent(this,"update-camera-dashboard");}}}},{kind:"method",key:"_goBack",value:function _goBack(ev){const backEvent=this.backEvent;const modelDatabase=backEvent.modelDatabase;if(modelDatabase){fireEvent(this,backEvent.event_name,{modelsInfo:modelDatabase});}else {fireEvent(this,backEvent.event_name);}}},{kind:"get",static:true,key:"styles",value:function styles(){return [r`
        @media all and (max-width: 450px), all and (max-height: 500px) {
          /* overrule the ha-style-dialog max-height on small screens */
          ha-dialog {
            --mdc-dialog-max-height: 100%;
            height: 100%;
          }
        }

        @media all and (min-width: 1000px) {
          ha-dialog {
            --mdc-dialog-min-width: 900px;
          }
        }

        @media all and (max-width: 450px), all and (max-height: 500px) {
          hui-entity-picker-table {
            height: calc(100vh - 158px);
          }
        }

        ha-dialog {
          --mdc-dialog-max-width: 500px;
          --dialog-content-padding: 2px 24px 20px 24px;
          --dialog-z-index: 5;
        }

        ha-header-bar {
          --mdc-theme-on-primary: var(--primary-text-color);
          --mdc-theme-primary: var(--mdc-theme-surface);
          flex-shrink: 0;
          border-bottom: 1px solid var(--mdc-dialog-scroll-divider-color, rgba(0, 0, 0, 0.12));
        }

        ha-form {
          margin-left: 8%;
          margin-right: 8%;
        }

        ha-formfield {
          display: flex;
          height: 56px;
          align-items: center;
          --mdc-typography-body2-font-size: 1em;
        }

        .button-confirm {
          background-color: #4ba2ff;
          float: right;
        }

        .button-back {
          --mdc-theme-primary: #7b7b7b;
          float: left;
          margin-left: 5%;
        }

        .form-issue {
          font-family: "Roboto";
          font-style: normal;
          font-size: 12px;
          color: #e41111;
          padding: 1% 1% 1% 12%;
          text-align: left;
          width: 100%;
        }

        .icon-back {
          width: 30px;
          height: 30px;
        }
        .form {
          margin-left: 10%;
          margin-right: 10%;
        }

        .header-text {
          font-family: "Roboto";
          font-style: normal;
          font-weight: 500;
          font-size: 36px;
          line-height: 42px;
          color: #303033;
          padding: 1% 1% 1% 5%;
          text-align: center;
          width: 38%;
        }

        .brand-list {
          display: grid;
          grid-template-columns: 1fr 1fr 1fr;
          grid-gap: 10%;
          padding: 0px 60px 30px 60px;
        }

        .cancel {
          cursor: pointer;
          padding: 20px 20px 20px 20px;
        }

        mwc-button {
          padding: 10px;
          text-align: center;
          text-decoration: none;
          display: inline-block;
          font-size: 16px;
          margin: 4px 2px;
          border-radius: 30px;
          cursor: pointer;
          box-shadow: 0px 0px 5px 0px rgba(1, 1, 1, 0);
          --mdc-theme-primary: white;
          margin-bottom: 40px;
        }

        .header_button {
          color: inherit;
          text-decoration: none;
        }

        mwc-tab-bar {
          border-bottom: 1px solid var(--mdc-dialog-scroll-divider-color, rgba(0, 0, 0, 0.12));
        }
        .cancel-icon {
          float: right;
          width: 40px;
          height: 40px;
        }
      `];}}]};},s);

export { HuiCreateDialogCameraFormulary };
