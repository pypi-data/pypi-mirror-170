const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, dI as fetchCameraInformation, f as fireEvent, $, dE as localize, z as o, dJ as mdiDelete, bC as mdiCheckboxMarkedCircle, dK as removeCamera, r, n } from './main-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-header-bar-dev.js';

let HuiDeleteDialogCamera=_decorate([n("delete-camera-dialog")],function(_initialize,_LitElement){class HuiDeleteDialogCamera extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiDeleteDialogCamera,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_params",value:void 0},{kind:"field",decorators:[t()],key:"cameraConfiguration",value:void 0},{kind:"field",decorators:[t()],key:"_currTabIndex",value(){return 0;}},{kind:"method",key:"showDialog",value:async function showDialog(params){this._params=params;this.cameraConfiguration=await fetchCameraInformation(this.hass,this._params.cameraInfo.entityID);}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._params=undefined;fireEvent(this,"dialog-closed",{dialog:this.localName});}},{kind:"method",key:"render",value:function render(){if(!this._params){return $``;}return $`
      <ha-dialog
        open
        scrimClickAction
        hideActions
        .heading=${localize("common.delete_camera")}
        class=${o({table:this._currTabIndex===1})}
        @closed=${this.closeDialog}
      >
        <div class="header" slot="heading">
          <ha-header-bar>
            <span slot="title">
              <ha-svg-icon class="header-icon" slot="icon" .path=${mdiDelete}></ha-svg-icon
            ></span>
          </ha-header-bar>
        </div>
        <div class="text">
          <p class="big-text">${localize("common.delete_camera")}</p>
          <p class="small-text">${localize("dialog_text.verify_action")}</p>
        </div>
        <div class="options">
          <mwc-button class="button-cancel" @click=${this._cancel}>
            ${localize("common.back")}</mwc-button
          >
          <mwc-button class="button-confirm" @click=${this._delete}
            ><ha-svg-icon
              class="confirm-icon"
              slot="icon"
              .path=${mdiCheckboxMarkedCircle}
            ></ha-svg-icon
            >${localize("common.confirm")}</mwc-button
          >
        </div>
      </ha-dialog>
    `;}},{kind:"method",key:"_cancel",value:function _cancel(ev){if(ev){ev.stopPropagation();}this.closeDialog();}},{kind:"method",key:"_delete",value:async function _delete(ev){if(ev){ev.stopPropagation();}const result=await removeCamera(this.hass,this.cameraConfiguration.unique_id,this.cameraConfiguration.entity_id);if(result===true){this.closeDialog();fireEvent(this,"update-camera-dashboard");}}},{kind:"get",static:true,key:"styles",value:function styles(){return [r`
        @media all and (max-width: 450px), all and (max-height: 500px) {
          /* overrule the ha-style-dialog max-height on small screens */
          ha-dialog {
            --mdc-dialog-max-height: 100%;
            height: 100%;
          }
        }

        @media all and (min-width: 800px) {
          ha-dialog {
            --mdc-dialog-min-width: 500px;
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

        .button-cancel {
          background-color: #a3abae;
          float: left;
          width: 22%;
        }

        .button-confirm {
          background-color: #4ba2ff;
          float: right;
        }
        .header {
          height: 80px;
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
        .confirm-icon {
          width: 20px;
          height: 40px;
        }
        .header-icon {
          width: 60px;
          height: 60px;
          padding-top: 50px;
          color: #7b7b7b;
        }
        .text {
          margin: 0px 0px 20px 0px;
        }
        .big-text {
          font-family: "Roboto";
          font-style: normal;
          font-weight: 500;
          font-size: 36px;
          line-height: 42px;
          color: #303033;
          margin: 10px;
        }
        .small-text {
          font-family: "Roboto";
          font-style: normal;
          font-weight: 400;
          font-size: 18px;
          line-height: 21px;
          color: #303033;
          margin: 10px;
        }
      `];}}]};},s);

export { HuiDeleteDialogCamera };
