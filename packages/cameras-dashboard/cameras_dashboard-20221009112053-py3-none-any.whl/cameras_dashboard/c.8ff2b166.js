import{_ as i,c as t,d as e,t as a,b as o,$ as c,f as n,n as s}from"./main-d07cb663.js";import{al as l,am as h,an as r,ao as d,ap as f,aq as u,C as m,e as p}from"./c.fc0bbf07.js";import"./c.ae68c3e2.js";import"./c.c8cf0377.js";import{a as g}from"./c.ebfe053a.js";import{c as _}from"./c.70b58286.js";import{b as v}from"./c.885af130.js";import"./c.95ef015c.js";import"./c.6c5cb033.js";import"./c.9c88d99b.js";import"./c.d294c310.js";import"./c.6dd7f489.js";import"./c.f2f631cd.js";import"./c.dd4b7d4a.js";import"./c.5fe2e3ab.js";import"./c.2036cb65.js";import"./c.65b9d701.js";import"./c.c245ec1a.js";import"./c.c9178224.js";import"./c.bd9a7167.js";import"./c.1ded644c.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.da136530.js";import"./c.fb31f48a.js";import"./c.2ff699c8.js";import"./c.379373ef.js";import"./c.650fd31d.js";import"./c.2465bf13.js";import"./c.3a0ccb1a.js";import"./c.f9f3b7e4.js";import"./c.ed8cead5.js";const b=l(v,h({entity:r(d()),name:r(d()),show_name:r(f()),icon:r(d()),show_icon:r(f()),icon_height:r(d()),tap_action:r(g),hold_action:r(g),theme:r(d()),show_state:r(f())})),j=["more-info","toggle","navigate","url","call-service","none"];let k=i([s("hui-button-card-editor")],(function(i,t){return{F:class extends t{constructor(...t){super(...t),i(this)}},d:[{kind:"field",decorators:[e({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[a()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(i){u(i,b),this._config=i}},{kind:"field",key:"_schema",value:()=>o(((i,t,e)=>[{name:"entity",selector:{entity:{domain:["light","switch","cover","automation","fan"]}}},{name:"",type:"grid",schema:[{name:"name",selector:{text:{}}},{name:"icon",selector:{icon:{placeholder:t||(null==e?void 0:e.attributes.icon),fallbackPath:t||null!=e&&e.attributes.icon||!e||!i?void 0:m(p(i),e)}}}]},{name:"",type:"grid",column_min_width:"100px",schema:[]},{name:"",type:"grid",schema:[]}]))},{kind:"get",key:"_tap_action",value:function(){return this._config.tap_action}},{kind:"get",key:"_hold_action",value:function(){return this._config.hold_action||{action:"more-info"}}},{kind:"method",key:"render",value:function(){var i;if(!this.hass||!this._config)return c``;const t=this._config.entity?this.hass.states[this._config.entity]:void 0,e=this._schema(this._config.entity,this._config.icon,t),a={show_name:!0,show_icon:!0,...this._config};return null!==(i=a.icon_height)&&void 0!==i&&i.includes("px")&&(a.icon_height=String(parseFloat(a.icon_height))),c`
      <ha-form
        .hass=${this.hass}
        .data=${a}
        .schema=${e}
        .computeLabel=${this._computeLabelCallback}
        @value-changed=${this._valueChanged}
      ></ha-form>
      <!-- <div class="card-config">
        <div class="side-by-side">
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.tap_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._tap_action}
            .actions=${j}
            .configValue=${"tap_action"}
            .tooltipText=${this.hass.localize("ui.panel.lovelace.editor.card.button.default_action_help")}
            @value-changed=${this._actionChanged}
          ></hui-action-editor>
          <hui-action-editor
            .label="${this.hass.localize("ui.panel.lovelace.editor.card.generic.hold_action")} (${this.hass.localize("ui.panel.lovelace.editor.card.config.optional")})"
            .hass=${this.hass}
            .config=${this._hold_action}
            .actions=${j}
            .configValue=${"hold_action"}
            .tooltipText=${this.hass.localize("ui.panel.lovelace.editor.card.button.default_action_help")}
            @value-changed=${this._actionChanged}
          ></hui-action-editor>
        </div>
      </div> -->
    `}},{kind:"method",key:"_valueChanged",value:function(i){const t=i.detail.value;t.icon_height&&!t.icon_height.endsWith("px")&&(t.icon_height+="px"),n(this,"config-changed",{config:t})}},{kind:"field",key:"_computeLabelCallback",value(){return i=>"entity"===i.name?`${this.hass.localize("ui.panel.lovelace.editor.card.generic.entity")}`:this.hass.localize(`ui.panel.lovelace.editor.card.generic.${i.name}`)}},{kind:"method",key:"_actionChanged",value:function(i){if(!this._config||!this.hass)return;const t=i.target,e=i.detail.value;if(this[`_${t.configValue}`]===e)return;let a;t.configValue&&(!1===e||e?a={...this._config,[t.configValue]:e}:(a={...this._config},delete a[t.configValue])),n(this,"config-changed",{config:a})}},{kind:"get",static:!0,key:"styles",value:function(){return _}}]}}),t);export{k as HuiButtonCardEditor};
