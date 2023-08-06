const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, f as fireEvent, b as memoizeOne, dD as Fuse, $, z as o, at as mdiClose, dE as localize, dF as mdiPlus, dG as defaultIntegration, r, n } from './main-dev.js';
import './ha-header-bar-dev.js';
import { c as customSchema, a as customCameraExtraOptionSchema } from './schemas-dev.js';
import './camera-brand-icon-button-dev.js';
import './search-input-round-dev.js';

let HuiCreateDialogCamera=_decorate([n("add-camera-dialog")],function(_initialize,_LitElement){class HuiCreateDialogCamera extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiCreateDialogCamera,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_cameraDatabase",value:void 0},{kind:"field",decorators:[t()],key:"_currTabIndex",value(){return 0;}},{kind:"field",decorators:[t()],key:"_filter",value(){return "";}},{kind:"method",key:"showDialog",value:async function showDialog(params){this._cameraDatabase=params.database.Manufacturer;}},{kind:"method",key:"closeDialog",value:function closeDialog(){this._cameraDatabase=undefined;this._currTabIndex=0;fireEvent(this,"dialog-closed",{dialog:this.localName});return true;}},{kind:"field",key:"_filterBrands",value(){return memoizeOne((cameraDatabase,filter)=>{if(!filter){return cameraDatabase;}let filteredBrands=cameraDatabase;const options={keys:["name"],//Add the possibility to search for model or other keys
isCaseSensitive:false,minMatchCharLength:1,threshold:0.2};const fuse=new Fuse(filteredBrands,options);filteredBrands=fuse.search(filter).map(result=>result.item);return filteredBrands;});}},{kind:"method",key:"render",value:function render(){if(!this._cameraDatabase){return $``;}const cameraDatabase=this._filterBrands(this._cameraDatabase,this._filter);return $`
      <ha-dialog
        open
        scrimClickAction
        hideActions
        @closed=${this.closeDialog}
        class=${o({table:this._currTabIndex===1})}
      >
        <div class="cancel">
          <ha-svg-icon
            @click=${this._cancel}
            class="cancel-icon"
            slot="icon"
            .path=${mdiClose}
          ></ha-svg-icon>
        </div>
        <div class="search-bar">
          <div class="add-camera">Add Camera</div>
          <search-input-round
            .hass=${this.hass}
            .filter=${this._filter}
            class="rounded"
            @value-changed=${this._handleSearchChange}
            .label=${localize("search.brands")}
          ></search-input-round>
        </div>

        <div class="brand-list">
          ${cameraDatabase.map(cameraBrandInfo=>{return $`<camera-brand-icon-button
              .cameraBrandInfo=${cameraBrandInfo}
              .label=${cameraBrandInfo.name}
              .cameraModelList=${cameraBrandInfo.models}
              @click=${()=>this._openCameraBrandDialog(cameraBrandInfo.models)}
            >
            </camera-brand-icon-button>`;})}
        </div>

        <div class="options">
          <mwc-button class="button-confirm" @click=${this._addCustomCamera}
            >${localize("common.custom_camera")}
            <ha-svg-icon slot="icon" .path=${mdiPlus}></ha-svg-icon
          ></mwc-button>
        </div>
      </ha-dialog>
    `;}},{kind:"method",key:"_openCameraBrandDialog",value:function _openCameraBrandDialog(cameraModelsList){this.closeDialog();fireEvent(this,"open-camera-brand-dialog",{modelsInfo:cameraModelsList});}},{kind:"method",key:"_addCustomCamera",value:function _addCustomCamera(){const form_schema={header:{title:localize("common.add_camera")},body:customSchema,extra_options:customCameraExtraOptionSchema,footer:{back:localize("common.go_back"),accept:localize("common.add_camera")}};fireEvent(this,"open-camera-add-camera-form",{cameraModelInfo:{},schema:form_schema,data:{integration:defaultIntegration},formType:"custom_camera",backEvent:{event_name:"add-new-camera"}});this.closeDialog();}},{kind:"method",key:"_handleSearchChange",value:function _handleSearchChange(ev){//Check hui-card-picker more information is required
this._filter=ev.detail.value;}},{kind:"method",key:"_cancel",value:function _cancel(ev){if(ev){ev.stopPropagation();}this.closeDialog();}},{kind:"get",static:true,key:"styles",value:function styles(){return [r`
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

        .button-confirm {
          background-color: #4ba2ff;
          float: right;
        }
        .search-bar {
          height: 80px;
          padding: 60px 45px 20px 45px;
        }
        search-input-round {
          float: right;
          display: block;
          width: 50%;
          margin-right: 10%;
        }

        .add-camera {
          float: left;
          font-family: "Roboto";
          font-style: normal;
          font-weight: 500;
          font-size: 36px;
          line-height: 42px;
          color: #303033;
          padding: 1% 1% 1% 1%;
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

        .cancel-icon {
          float: right;
          width: 40px;
          height: 40px;
        }
      `];}}]};},s);

export { HuiCreateDialogCamera };
