import{_ as a,$ as e,j as s,k as i,f as t,n as c}from"./main-d07cb663.js";import{al as o,am as r,as as l,aw as m,an as n,ao as d,ap as p,aq as f}from"./c.fc0bbf07.js";import{b as h}from"./c.885af130.js";import{HuiStackCardEditor as u}from"./c.a027e673.js";import"./c.95ef015c.js";import"./c.37525831.js";import"./c.c11921c6.js";import"./c.62305b3f.js";import"./c.0ab76581.js";import"./c.c183f332.js";import"./c.fdc46b67.js";import"./c.c17eba9f.js";import"./c.5fe2e3ab.js";import"./c.6dd7f489.js";import"./c.c8cf0377.js";import"./c.9c88d99b.js";import"./c.a777a267.js";import"./c.6da20489.js";import"./c.ed8cead5.js";import"./c.379373ef.js";import"./c.b0065faf.js";import"./c.ebfe053a.js";import"./c.70b58286.js";const j=o(h,r({cards:l(m()),title:n(d()),square:n(p()),columns:n(d())}));let b=a([c("hui-grid-card-editor")],(function(a,c){class o extends c{constructor(...e){super(...e),a(this)}}return{F:o,d:[{kind:"method",key:"setConfig",value:function(a){f(a,j),this._config=a}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return e``;const a=[{type:"grid",name:"",schema:[{name:"columns",selector:{select:{options:[{value:"1",label:this.hass.localize("ui.panel.lovelace.editor.card.grid.big")},{value:"2",label:this.hass.localize("ui.panel.lovelace.editor.card.grid.medium")},{value:"3",label:this.hass.localize("ui.panel.lovelace.editor.card.grid.small")}]}}},{name:"title",selector:{text:{}}}]}],t={title:"",square:!0,columns:"3",...this._config};return e`
      <div class="formContainer" style="width:90%;margin-left:5%">
        <ha-form
          .hass=${this.hass}
          .data=${t}
          .schema=${a}
          .computeLabel=${this._computeLabelCallback}
          @value-changed=${this._valueChanged}
        ></ha-form>
      </div>
      ${s(i(o.prototype),"render",this).call(this)}
    `}},{kind:"method",key:"_valueChanged",value:function(a){t(this,"config-changed",{config:a.detail.value})}},{kind:"field",key:"_computeLabelCallback",value(){return a=>this.hass.localize(`ui.panel.lovelace.editor.card.grid.${a.name}`)}}]}}),u);export{b as HuiGridCardEditor};
