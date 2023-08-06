const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, dE as localize, dI as fetchCameraInformation, dL as getCameraEntities, f as fireEvent, $, z as o, at as mdiClose, dM as updateCameraInformation, r, n } from './main-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-header-bar-dev.js';
import './ha-form-dev.js';
import { c as customSchema, a as customCameraExtraOptionSchema } from './schemas-dev.js';
import './camera-brand-icon-button-dev.js';
import './search-input-round-dev.js';
import './dynamic-element-directive-dev.js';
import './stop_propagation-dev.js';
import './ha-checkbox-dev.js';
import './mwc-checkbox.css-dev.js';
import './ha-check-list-item-dev.js';
import './ha-base-time-input-dev.js';

let HuiEditDialogCamera=_decorate([n("edit-camera-dialog")],function(_initialize,_LitElement){class HuiEditDialogCamera extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiEditDialogCamera,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"dialogOpen",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"cameraInfo",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"backEvent",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"registeredCameras",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"schema",value:void 0},{kind:"field",decorators:[t()],key:"_currTabIndex",value(){return 0;}},{kind:"field",decorators:[t()],key:"validIssue",value:void 0},{kind:"method",key:"showDialog",value:async function showDialog(params){const form_schema={header:{title:localize("common.add_camera")},body:customSchema,extra_options:customCameraExtraOptionSchema,footer:{accept:localize("common.edit_camera")}};this._params=params;this.schema=form_schema;this.dialogOpen=true;this.cameraInfo=await fetchCameraInformation(this.hass,this._params.cameraInfo.entityID);this.registeredCameras=getCameraEntities(this.hass.states).map(camera=>camera.name);if(this.cameraInfo.authentication!==undefined){this.cameraInfo.authentication=this.cameraInfo.authentication[0].toUpperCase()+this.cameraInfo.authentication.substring(1);}if(this.cameraInfo.verify_ssl!=undefined){let verify_ssl=this.cameraInfo.verify_ssl;verify_ssl=String(this.cameraInfo.verify_ssl);this.cameraInfo.verify_ssl=verify_ssl[0].toUpperCase()+verify_ssl.substring(1);}}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._currTabIndex=0;this.dialogOpen=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});return true;}},{kind:"method",key:"render",value:function render(){if(this.cameraInfo===undefined||!this.dialogOpen){return $``;}const schemaBody=this.schema.body;const schemaExtraOptions=this.schema.extra_options;return $` <ha-dialog
      open
      scrimClickAction
      hideActions
      class=${o({table:this._currTabIndex===1})}
      @closed=${this.closeDialog}
    >
      <div class="cancel">
        <ha-svg-icon
          dialogAction="close"
          class="cancel-icon"
          slot="icon"
          .path=${mdiClose}
        ></ha-svg-icon>
      </div>
      <div class="header-text">${localize("common.edit_camera")}</div>
      </div>
      ${this.validIssue?$` <div class="form-issue">${this.validIssue}</div>`:$``}
      <div class="form">
      <ha-form
            .hass=${this.hass}
            .data=${this.cameraInfo}
            .schema=${schemaBody}
            .computeLabel=${this._computeLabelCallback}
            @value-changed=${this._valueChanged}
          ></ha-form>
          ${schemaExtraOptions&&this.cameraInfo.advanced_options?$` <ha-form
                  .hass=${this.hass}
                  .data=${this.cameraInfo}
                  .schema=${schemaExtraOptions}
                  .computeLabel=${this._computeLabelCallback}
                  @value-changed=${this._valueChanged}
                ></ha-form>`:$``}
        </div>
        <div class="options">
          <mwc-button class="button-confirm" @click=${this._accept}
            >${this.schema.footer.accept}</mwc-button
          >
        </div>
    </ha-dialog>`;}},{kind:"field",key:"_computeLabelCallback",value(){return schema=>{return localize(`form.${schema.name}`);};}},{kind:"method",key:"_valueChanged",value:function _valueChanged(ev){const config=ev.detail.value;this.cameraInfo={...this.cameraInfo,...config};}},{kind:"method",key:"_accept",value:async function _accept(){const valid=this.validInput();if(valid===true){const camInfo=this.removeNull(this.cameraInfo);const result=await updateCameraInformation(this.hass,camInfo);if(result===true){this.closeDialog();fireEvent(this,"update-camera-dashboard");}}}},{kind:"method",key:"validInput",value:function validInput(){if(!this.cameraInfo.integration){this.validIssue=localize("form.issues.missing_integration");return false;}if(!this.cameraInfo.name){this.validIssue=localize("form.issues.camera_name");return false;}if(this.registeredCameras.includes(this.cameraInfo.camera_name)){this.validIssue=localize("form.issues.duplicated_camera_name");return false;}if(!this.cameraInfo.still_image_url&&!this.cameraInfo.stream_source){this.validIssue=localize("form.issues.static_stream_source_missing");return false;}return true;}},{kind:"method",key:"removeNull",value:function removeNull(cameraInfo){//Remove null keys in the dictionary (ensuring the data passes the checks in the backend. This is not the most elegant solution but it should work for now)
for(const[key,value]of Object.entries(cameraInfo)){if(value===null){delete cameraInfo[key];}}return cameraInfo;}},{kind:"get",static:true,key:"styles",value:function styles(){return [r`
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

export { HuiEditDialogCamera };
