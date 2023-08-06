const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { _ as _decorate, c as s, d as e, t, j as _get, k as _getPrototypeOf, $, z as o, S as applyThemesOnElement, r, n } from './main-dev.js';
import './ha-markdown-dev.js';

const subscribeRenderTemplate=(conn,onChange,params)=>conn.subscribeMessage(msg=>onChange(msg),{type:"render_template",...params});

let HuiMarkdownCard=_decorate([n("hui-markdown-card")],function(_initialize,_LitElement){class HuiMarkdownCard extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:HuiMarkdownCard,d:[{kind:"method",static:true,key:"getConfigElement",value:async function getConfigElement(){await import('./hui-markdown-card-editor-dev.js');return document.createElement("hui-markdown-card-editor");}},{kind:"method",static:true,key:"getStubConfig",value:function getStubConfig(){return {type:"markdown",content:"The **Markdown** card allows you to write any text. You can style it **bold**, *italicized*, ~strikethrough~ etc. You can do images, links, and more.\n\nFor more information see the [Markdown Cheatsheet](https://commonmark.org/help)."};}},{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[t()],key:"_config",value:void 0},{kind:"field",decorators:[t()],key:"_templateResult",value:void 0},{kind:"field",decorators:[t()],key:"_unsubRenderTemplate",value:void 0},{kind:"method",key:"getCardSize",value:function getCardSize(){return this._config===undefined?3:this._config.card_size===undefined?Math.round(this._config.content.split("\n").length/2)+(this._config.title?1:0):this._config.card_size;}},{kind:"method",key:"setConfig",value:function setConfig(config){var _this$_config;if(!config.content){return {type:"markdown",content:" "};}if(((_this$_config=this._config)===null||_this$_config===void 0?void 0:_this$_config.content)!==config.content){this._tryDisconnect();}this._config=config;}},{kind:"method",key:"connectedCallback",value:function connectedCallback(){_get(_getPrototypeOf(HuiMarkdownCard.prototype),"connectedCallback",this).call(this);this._tryConnect();}},{kind:"method",key:"disconnectedCallback",value:function disconnectedCallback(){this._tryDisconnect();}},{kind:"method",key:"render",value:function render(){var _this$_templateResult;if(!this._config){return $``;}return $`
      <ha-card .header=${this._config.title}>
        <ha-markdown
          breaks
          class=${o({"no-header":!this._config.title})}
          .content=${(_this$_templateResult=this._templateResult)===null||_this$_templateResult===void 0?void 0:_this$_templateResult.result}
        ></ha-markdown>
      </ha-card>
    `;}},{kind:"method",key:"updated",value:function updated(changedProps){_get(_getPrototypeOf(HuiMarkdownCard.prototype),"updated",this).call(this,changedProps);if(!this._config||!this.hass){return;}this._tryConnect();const oldHass=changedProps.get("hass");const oldConfig=changedProps.get("_config");if(!oldHass||!oldConfig||oldHass.themes!==this.hass.themes||oldConfig.theme!==this._config.theme){applyThemesOnElement(this,this.hass.themes,this._config.theme);}}},{kind:"method",key:"_tryConnect",value:async function _tryConnect(){if(this._unsubRenderTemplate!==undefined||!this.hass||!this._config){return;}try{this._unsubRenderTemplate=subscribeRenderTemplate(this.hass.connection,result=>{this._templateResult=result;},{template:this._config.content,entity_ids:this._config.entity_id,variables:{config:this._config,user:this.hass.user.name}});}catch(_err){this._templateResult={result:this._config.content,listeners:{all:false,domains:[],entities:[],time:false}};this._unsubRenderTemplate=undefined;}}},{kind:"method",key:"_tryDisconnect",value:async function _tryDisconnect(){if(!this._unsubRenderTemplate){return;}try{const unsub=await this._unsubRenderTemplate;unsub();this._unsubRenderTemplate=undefined;}catch(err){if(err.code==="not_found");else {throw err;}}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      ha-card {
        height: 100%;
        border-radius: 1.5rem;
      }
      ha-markdown {
        padding: 0 16px 16px;
        word-wrap: break-word;
      }
      ha-markdown.no-header {
        padding-top: 16px;
      }
    `;}}]};},s);

export { HuiMarkdownCard };
