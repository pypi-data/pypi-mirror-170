import{ew as i,ex as e,cR as t,cS as s,an as a,ey as n,_ as o,c as r,d as c,t as d,b as h,$ as u,z as l,j as f,k as _,S as m,r as v,n as g}from"./main-d07cb663.js";import{C as p,e as b,h as k,S as y,f as $,ac as x,k as j}from"./c.fc0bbf07.js";import{v as w}from"./c.37525831.js";import{s as S}from"./c.c13d4687.js";import{a as z,s as A}from"./c.2036cb65.js";import{S as I}from"./c.65b9d701.js";import"./c.95ef015c.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";import"./c.d294c310.js";const D=["sensor"],N=["binary_sensor"],B=["light","switch","fan"],C=["camera"],E={sensor:["temperature"],binary_sensor:["motion"]},O={light:{on:i,off:e},switch:{on:t,off:s},fan:{on:p("fan"),off:p("fan")},sensor:{humidity:a},binary_sensor:{motion:n}};let R=o([g("hui-area-card")],(function(i,e){class t extends e{constructor(...e){super(...e),i(this)}}return{F:t,d:[{kind:"method",static:!0,key:"getConfigElement",value:async function(){return await import("./c.51175d2a.js"),document.createElement("hui-area-card-editor")}},{kind:"method",static:!0,key:"getStubConfig",value:async function(i){var e;return{type:"area",area:(null===(e=(await S(i.connection,z))[0])||void 0===e?void 0:e.area_id)||""}}},{kind:"field",decorators:[c({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[d()],key:"_config",value:void 0},{kind:"field",decorators:[d()],key:"_entities",value:void 0},{kind:"field",decorators:[d()],key:"_devices",value:void 0},{kind:"field",decorators:[d()],key:"_areas",value:void 0},{kind:"field",key:"_entitiesByDomain",value:()=>h(((i,e,t,s)=>{const a=t.filter((t=>!t.entity_category&&(t.area_id?t.area_id===i:t.device_id&&e.has(t.device_id)))).map((i=>i.entity_id)),n={};for(const i of a){const e=b(i);if(!(B.includes(e)||D.includes(e)||N.includes(e)||C.includes(e)))continue;const t=s[i];t&&((!D.includes(e)&&!N.includes(e)||E[e].includes(t.attributes.device_class||""))&&(e in n||(n[e]=[]),n[e].push(t)))}return n}))},{kind:"method",key:"_isOn",value:function(i,e){const t=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states)[i];if(t)return(e?t.filter((i=>i.attributes.device_class===e)):t).some((i=>!k.includes(i.state)&&!y.includes(i.state)))}},{kind:"method",key:"_average",value:function(i,e){const t=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states)[i].filter((i=>!e||i.attributes.device_class===e));if(!t)return;let s;const a=t.filter((i=>!(!i.attributes.unit_of_measurement||isNaN(Number(i.state)))&&(s?i.attributes.unit_of_measurement===s:(s=i.attributes.unit_of_measurement,!0))));if(!a.length)return;const n=a.reduce(((i,e)=>i+Number(e.state)),0);return`${$(n/a.length,this.hass.locale,{maximumFractionDigits:1})} ${s}`}},{kind:"field",key:"_area",value:()=>h(((i,e)=>e.find((e=>e.area_id===i))||null))},{kind:"field",key:"_devicesInArea",value:()=>h(((i,e)=>new Set(i?e.filter((e=>e.area_id===i)).map((i=>i.id)):[])))},{kind:"method",key:"hassSubscribe",value:function(){return[z(this.hass.connection,(i=>{this._areas=i})),A(this.hass.connection,(i=>{this._devices=i})),x(this.hass.connection,(i=>{this._entities=i}))]}},{kind:"method",key:"getCardSize",value:function(){return 3}},{kind:"method",key:"setConfig",value:function(i){if(!i.area)throw new Error("Area Required");this._config=i}},{kind:"method",key:"shouldUpdate",value:function(i){if(i.has("_config")||!this._config)return!0;if(i.has("_devicesInArea")||i.has("_areas")||i.has("_entities"))return!0;if(!i.has("hass"))return!1;const e=i.get("hass");if(!e||e.themes!==this.hass.themes||e.locale!==this.hass.locale)return!0;if(!this._devices||!this._devicesInArea(this._config.area,this._devices)||!this._entities)return!1;const t=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states);for(const i of Object.values(t))for(const t of i)if(e.states[t.entity_id]!==t)return!0;return!1}},{kind:"method",key:"render",value:function(){if(!(this._config&&this.hass&&this._areas&&this._devices&&this._entities))return u``;const i=this._entitiesByDomain(this._config.area,this._devicesInArea(this._config.area,this._devices),this._entities,this.hass.states),e=this._area(this._config.area,this._areas);if(null===e)return u`
        <hui-warning>
          ${this.hass.localize("ui.card.area.area_not_found")}
        </hui-warning>
      `;const t=[];let s;return D.forEach((e=>{e in i&&E[e].forEach((s=>{i[e].some((i=>i.attributes.device_class===s))&&t.push(u`
            ${O[e][s]?u`<ha-svg-icon
                  .path=${O[e][s]}
                ></ha-svg-icon>`:""}
            ${this._average(e,s)}
          `)}))})),this._config.show_camera&&"camera"in i&&(s=i.camera[0].entity_id),u`
      <ha-card class=${e.picture||s?"image":""}>
        ${e.picture||s?u`<hui-image
              .config=${this._config}
              .hass=${this.hass}
              .image=${e.picture?e.picture:void 0}
              .cameraImage=${s}
              aspectRatio="16:9"
            ></hui-image>`:""}

        <div
          class="container ${l({navigate:void 0!==this._config.navigation_path})}"
          @click=${this._handleNavigation}
        >
          <div class="alerts">
            ${N.map((e=>e in i?E[e].map((i=>this._isOn(e,i)?u`
                      ${O[e][i]?u`<ha-svg-icon
                            .path=${O[e][i]}
                          ></ha-svg-icon>`:""}
                    `:"")):""))}
          </div>
          <div class="bottom">
            <div>
              <div class="name">${e.name}</div>
              ${t.length?u`<div class="sensors">${t}</div>`:""}
            </div>
            <div class="buttons">
              ${B.map((e=>{if(!(e in i))return"";const t=this._isOn(e);return B.includes(e)?u`
                      <ha-icon-button
                        class=${t?"on":"off"}
                        .path=${O[e][t?"on":"off"]}
                        .domain=${e}
                        @click=${this._toggle}
                      >
                      </ha-icon-button>
                    `:""}))}
            </div>
          </div>
        </div>
      </ha-card>
    `}},{kind:"method",key:"updated",value:function(i){if(f(_(t.prototype),"updated",this).call(this,i),!this._config||!this.hass)return;const e=i.get("hass"),s=i.get("_config");(!i.has("hass")||e&&e.themes===this.hass.themes)&&(!i.has("_config")||s&&s.theme===this._config.theme)||m(this,this.hass.themes,this._config.theme)}},{kind:"method",key:"_handleNavigation",value:function(){this._config.navigation_path&&w(this._config.navigation_path)}},{kind:"method",key:"_toggle",value:function(i){i.stopPropagation();const e=i.currentTarget.domain;B.includes(e)&&this.hass.callService(e,this._isOn(e)?"turn_off":"turn_on",void 0,{area_id:this._config.area}),j("light")}},{kind:"get",static:!0,key:"styles",value:function(){return v`
      ha-card {
        overflow: hidden;
        position: relative;
        padding-bottom: 56.25%;
        background-size: cover;
      }

      ha-card.image {
        padding-bottom: 0;
      }

      .container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: linear-gradient(
          0,
          rgba(33, 33, 33, 0.9) 0%,
          rgba(33, 33, 33, 0) 45%
        );
      }

      ha-card:not(.image) .container::before {
        position: absolute;
        content: "";
        width: 100%;
        height: 100%;
        background-color: var(--sidebar-selected-icon-color);
        opacity: 0.12;
      }

      .sensors {
        color: #e3e3e3;
        font-size: 16px;
        --mdc-icon-size: 24px;
        opacity: 0.6;
        margin-top: 8px;
      }

      .alerts {
        padding: 16px;
      }

      .alerts ha-svg-icon {
        background: var(--accent-color);
        color: var(--text-accent-color, var(--text-primary-color));
        padding: 8px;
        border-radius: 50%;
      }

      .name {
        color: white;
        font-size: 24px;
      }

      .bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px;
      }

      .navigate {
        cursor: pointer;
      }

      ha-icon-button {
        color: white;
        background-color: var(--area-button-color, #727272b2);
        border-radius: 50%;
        margin-left: 8px;
        --mdc-icon-button-size: 44px;
      }
      .on {
        color: var(--paper-item-icon-active-color, #fdd835);
      }
    `}}]}}),I(r));export{R as HuiAreaCard};
