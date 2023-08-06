import{_ as e,l as t,d as n,j as r,k as a,f as o,n as s,c as i,$ as c,r as l}from"./main-d07cb663.js";const d=Symbol("Comlink.proxy"),u=Symbol("Comlink.endpoint"),m=Symbol("Comlink.releaseProxy"),h=Symbol("Comlink.thrown"),p=e=>"object"==typeof e&&null!==e||"function"==typeof e,k=new Map([["proxy",{canHandle:e=>p(e)&&e[d],serialize(e){const{port1:t,port2:n}=new MessageChannel;return f(e,t),[n,[n]]},deserialize:e=>(e.start(),v(e))}],["throw",{canHandle:e=>p(e)&&h in e,serialize({value:e}){let t;return t=e instanceof Error?{isError:!0,value:{message:e.message,name:e.name,stack:e.stack}}:{isError:!1,value:e},[t,[]]},deserialize(e){if(e.isError)throw Object.assign(new Error(e.value.message),e.value);throw e.value}}]]);function f(e,t=self){t.addEventListener("message",(function n(r){if(!r||!r.data)return;const{id:a,type:o,path:s}=Object.assign({path:[]},r.data),i=(r.data.argumentList||[]).map(L);let c;try{const t=s.slice(0,-1).reduce(((e,t)=>e[t]),e),n=s.reduce(((e,t)=>e[t]),e);switch(o){case"GET":c=n;break;case"SET":t[s.slice(-1)[0]]=L(r.data.value),c=!0;break;case"APPLY":c=n.apply(t,i);break;case"CONSTRUCT":c=function(e){return Object.assign(e,{[d]:!0})}(new n(...i));break;case"ENDPOINT":{const{port1:t,port2:n}=new MessageChannel;f(e,n),c=function(e,t){return E.set(e,t),e}(t,[t])}break;case"RELEASE":c=void 0;break;default:return}}catch(e){c={value:e,[h]:0}}Promise.resolve(c).catch((e=>({value:e,[h]:0}))).then((e=>{const[r,s]=S(e);t.postMessage(Object.assign(Object.assign({},r),{id:a}),s),"RELEASE"===o&&(t.removeEventListener("message",n),g(t))}))})),t.start&&t.start()}function g(e){(function(e){return"MessagePort"===e.constructor.name})(e)&&e.close()}function v(e,t){return w(e,[],t)}function y(e){if(e)throw new Error("Proxy has been released and is not useable")}function w(e,t=[],n=function(){}){let r=!1;const a=new Proxy(n,{get(n,o){if(y(r),o===m)return()=>T(e,{type:"RELEASE",path:t.map((e=>e.toString()))}).then((()=>{g(e),r=!0}));if("then"===o){if(0===t.length)return{then:()=>a};const n=T(e,{type:"GET",path:t.map((e=>e.toString()))}).then(L);return n.then.bind(n)}return w(e,[...t,o])},set(n,a,o){y(r);const[s,i]=S(o);return T(e,{type:"SET",path:[...t,a].map((e=>e.toString())),value:s},i).then(L)},apply(n,a,o){y(r);const s=t[t.length-1];if(s===u)return T(e,{type:"ENDPOINT"}).then(L);if("bind"===s)return w(e,t.slice(0,-1));const[i,c]=b(o);return T(e,{type:"APPLY",path:t.map((e=>e.toString())),argumentList:i},c).then(L)},construct(n,a){y(r);const[o,s]=b(a);return T(e,{type:"CONSTRUCT",path:t.map((e=>e.toString())),argumentList:o},s).then(L)}});return a}function b(e){const t=e.map(S);return[t.map((e=>e[0])),(n=t.map((e=>e[1])),Array.prototype.concat.apply([],n))];var n}const E=new WeakMap;function S(e){for(const[t,n]of k)if(n.canHandle(e)){const[r,a]=n.serialize(e);return[{type:"HANDLER",name:t,value:r},a]}return[{type:"RAW",value:e},E.get(e)||[]]}function L(e){switch(e.type){case"HANDLER":return k.get(e.name).deserialize(e.value);case"RAW":return e.value}}function T(e,t,n){return new Promise((r=>{const a=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");e.addEventListener("message",(function t(n){n.data&&n.data.id&&n.data.id===a&&(e.removeEventListener("message",t),r(n.data))})),e.start&&e.start(),e.postMessage(Object.assign({id:a},t),n)}))}let M;e([s("ha-markdown-element")],(function(e,t){class s extends t{constructor(...t){super(...t),e(this)}}return{F:s,d:[{kind:"field",decorators:[n()],key:"content",value:void 0},{kind:"field",decorators:[n({type:Boolean})],key:"allowSvg",value:()=>!1},{kind:"field",decorators:[n({type:Boolean})],key:"breaks",value:()=>!1},{kind:"method",key:"createRenderRoot",value:function(){return this}},{kind:"method",key:"update",value:function(e){r(a(s.prototype),"update",this).call(this,e),void 0!==this.content&&this._render()}},{kind:"method",key:"_render",value:async function(){this.innerHTML=await(async(e,t,n)=>(M||(M=v(new Worker(new URL("./markdown_worker",import.meta.url)))),M.renderMarkdown(e,t,n)))(String(this.content),{breaks:this.breaks,gfm:!0},{allowSvg:this.allowSvg});const e=document.createTreeWalker(this,NodeFilter.SHOW_ELEMENT,null);for(;e.nextNode();){const t=e.currentNode;t instanceof HTMLAnchorElement&&t.host!==document.location.host?(t.target="_blank",t.rel="noreferrer noopener"):t instanceof HTMLImageElement&&t.addEventListener("load",this._resize)}}},{kind:"field",key:"_resize",value(){return()=>o(this,"iron-resize")}}]}}),t),e([s("ha-markdown")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[n()],key:"content",value:void 0},{kind:"field",decorators:[n({type:Boolean})],key:"allowSvg",value:()=>!1},{kind:"field",decorators:[n({type:Boolean})],key:"breaks",value:()=>!1},{kind:"method",key:"render",value:function(){return this.content?c`<ha-markdown-element
      .content=${this.content}
      .allowSvg=${this.allowSvg}
      .breaks=${this.breaks}
    ></ha-markdown-element>`:c``}},{kind:"get",static:!0,key:"styles",value:function(){return l`
      :host {
        display: block;
      }
      ha-markdown-element {
        -ms-user-select: text;
        -webkit-user-select: text;
        -moz-user-select: text;
      }
      ha-markdown-element > *:first-child {
        margin-top: 0;
      }
      ha-markdown-element > *:last-child {
        margin-bottom: 0;
      }
      a {
        color: var(--accent-color);
      }
      img {
        max-width: 100%;
      }
      code,
      pre {
        background-color: var(--markdown-code-background-color, none);
        border-radius: 3px;
      }
      svg {
        background-color: var(--markdown-svg-background-color, none);
        color: var(--markdown-svg-color, none);
      }
      code {
        font-size: 85%;
        padding: 0.2em 0.4em;
      }
      pre code {
        padding: 0;
      }
      pre {
        padding: 16px;
        overflow: auto;
        line-height: 1.45;
        font-family: var(--code-font-family, monospace);
      }
      h1,
      h2,
      h3,
      h4,
      h5,
      h6 {
        line-height: initial;
      }
      h2 {
        font-size: 1.5em;
        font-weight: bold;
      }
    `}}]}}),i);
