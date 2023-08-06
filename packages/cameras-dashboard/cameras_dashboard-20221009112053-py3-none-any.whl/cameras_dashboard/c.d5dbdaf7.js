import{_ as i,c as e,d as t,t as a,$ as c,f as o,n as s}from"./main-d07cb663.js";import"./c.ae68c3e2.js";import"./c.c8cf0377.js";import{al as n,am as r,an as d,ao as l,as as h,aq as f}from"./c.fc0bbf07.js";import"./c.25c3182d.js";import{p as m}from"./c.9bf416cd.js";import{a as g}from"./c.ebfe053a.js";import{b as u}from"./c.885af130.js";import{e as p}from"./c.b0065faf.js";import{c as _}from"./c.70b58286.js";import"./c.95ef015c.js";import"./c.6c5cb033.js";import"./c.9c88d99b.js";import"./c.d294c310.js";import"./c.6dd7f489.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.5fe2e3ab.js";import"./c.2036cb65.js";import"./c.65b9d701.js";import"./c.c245ec1a.js";import"./c.c9178224.js";import"./c.bd9a7167.js";import"./c.1ded644c.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.da136530.js";import"./c.fb31f48a.js";import"./c.2ff699c8.js";import"./c.379373ef.js";import"./c.650fd31d.js";import"./c.2465bf13.js";import"./c.3a0ccb1a.js";import"./c.f9f3b7e4.js";import"./c.ed8cead5.js";const v=n(u,r({title:d(l()),entity:d(l()),image:d(l()),camera_image:d(l()),camera_view:d(l()),aspect_ratio:d(l()),tap_action:d(g),hold_action:d(g),entities:h(p),theme:d(l())})),j=["more-info","toggle","navigate","call-service","none"],b=[{name:"title",selector:{text:{}}},{name:"image",selector:{text:{}}},{name:"camera_image",selector:{entity:{domain:"camera"}}},{name:"",type:"grid",schema:[{name:"camera_view",selector:{select:{options:["auto","live"]}}},{name:"aspect_ratio",selector:{text:{}}}]},{name:"entity",selector:{entity:{}}}];let k=i([s("hui-picture-glance-card-editor")],(function(i,e){return{F:class extends e{constructor(...e){super(...e),i(this)}},d:[{kind:"field",decorators:[t({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"_config",value:void 0},{kind:"field",decorators:[a()],key:"_configEntities",value:void 0},{kind:"method",key:"setConfig",value:function(i){f(i,v),this._config=i,this._configEntities=m(i.entities)}},{kind:"get",key:"_tap_action",value:function(){return this._config.tap_action||{action:"toggle"}}},{kind:"get",key:"_hold_action",value:function(){return this._config.hold_action||{action:"more-info"}}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return c``;const i={camera_view:"auto",...this._config};return c`
      <ha-form
        .hass=${this.hass}
        .data=${i}
        .schema=${b}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <div class="card-config">
        <div class="side-by-side">
          <hui-action-editor
            .label=${this.hass.localize("ui.panel.lovelace.editor.card.generic.tap_action")}
            .hass=${this.hass}
            .config=${this._tap_action}
            .actions=${j}
            .configValue=${"tap_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
          <hui-action-editor
            .label=${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")}
            .hass=${this.hass}
            .config=${this._hold_action}
            .actions=${j}
            .configValue=${"hold_action"}
            @value-changed=${this._valueChanged}
          ></hui-action-editor>
        </div>
        <hui-entity-editor
          .hass=${this.hass}
          .entities=${this._configEntities}
          @entities-changed=${this._changed}
        ></hui-entity-editor>
      </div>
    `}},{kind:"method",key:"_valueChanged",value:function(i){o(this,"config-changed",{config:i.detail.value})}},{kind:"method",key:"_changed",value:function(i){if(!this._config||!this.hass)return;const e=i.target,t=i.detail.value;if(i.detail&&i.detail.entities)this._config={...this._config,entities:i.detail.entities},this._configEntities=m(this._config.entities);else if(e.configValue){if(this[`_${e.configValue}`]===t)return;!1===t||t?this._config={...this._config,[e.configValue]:t}:(this._config={...this._config},delete this._config[e.configValue])}o(this,"config-changed",{config:this._config})}},{kind:"field",key:"_computeLabelCallback",value(){return i=>"entity"===i.name?this.hass.localize("ui.panel.lovelace.editor.card.picture-glance.state_entity"):this.hass.localize(`ui.panel.lovelace.editor.card.generic.${i.name}`)||this.hass.localize(`ui.panel.lovelace.editor.card.picture-glance.${i.name}`)}},{kind:"field",static:!0,key:"styles",value:()=>_}]}}),e);export{k as HuiPictureGlanceCardEditor};
