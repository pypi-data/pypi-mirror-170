import{_ as e,c as t,d as i,t as s,j as a,k as o,S as r,$ as n,r as h,n as c}from"./main-d07cb663.js";import{W as m,ar as d}from"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.fc0bbf07.js";import"./c.95ef015c.js";import"./c.0ab76581.js";import"./c.c183f332.js";e([c("hui-picture-elements-card")],(function(e,t){class c extends t{constructor(...t){super(...t),e(this)}}return{F:c,d:[{kind:"field",decorators:[i({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[s()],key:"_elements",value:void 0},{kind:"method",static:!0,key:"getStubConfig",value:function(e,t,i){return{type:"picture-elements",elements:[{type:"state-badge",entity:m(e,1,t,i,["sensor","binary_sensor"])[0]||"",style:{top:"32%",left:"40%"}}],image:"https://demo.home-assistant.io/stub_config/floorplan.png"}}},{kind:"field",decorators:[s()],key:"_config",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 4}},{kind:"method",key:"setConfig",value:function(e){if(!e)throw new Error("Invalid configuration");if(!(e.image||e.camera_image||e.state_image)||e.state_image&&!e.entity)throw new Error("Image required");if(!Array.isArray(e.elements))throw new Error("Elements required");this._config=e,this._elements=this._config.elements.map((e=>{const t=d(e);return this.hass&&(t.hass=this.hass),t}))}},{kind:"method",key:"updated",value:function(e){if(a(o(c.prototype),"updated",this).call(this,e),!this._config||!this.hass)return;if(this._elements&&e.has("hass"))for(const e of this._elements)e.hass=this.hass;const t=e.get("hass"),i=e.get("_config");t&&i&&t.themes===this.hass.themes&&i.theme===this._config.theme||r(this,this.hass.themes,this._config.theme)}},{kind:"method",key:"render",value:function(){return this.hass&&this._config?n`
      <ha-card .header=${this._config.title}>
        <div id="root">
          <hui-image
            .hass=${this.hass}
            .image=${this._config.image}
            .stateImage=${this._config.state_image}
            .stateFilter=${this._config.state_filter}
            .cameraImage=${this._config.camera_image}
            .cameraView=${this._config.camera_view}
            .entity=${this._config.entity}
            .aspectRatio=${this._config.aspect_ratio}
            .darkModeFilter=${this._config.dark_mode_filter}
            .darkModeImage=${this._config.dark_mode_image}
          ></hui-image>
          ${this._elements}
        </div>
      </ha-card>
    `:n``}},{kind:"get",static:!0,key:"styles",value:function(){return h`
      #root {
        position: relative;
      }

      .element {
        position: absolute;
        transform: translate(-50%, -50%);
      }

      ha-card {
        overflow: hidden;
        height: 100%;
        box-sizing: border-box;
      }
    `}}]}}),t);
