const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { P as PolymerElement, q as html, dZ as hs2rgb, d_ as rgb2hs, _ as _decorate, c as s, d as e, t, $, z as o, b3 as mdiPalette, j as _get, k as _getPrototypeOf, b as memoizeOne, r, n } from './main-dev.js';
import { E as EventsMixin, n as lightSupportsDimming, o as computeStateDisplay, p as lightSupportsColorMode, L as LightColorModes, q as lightSupportsColor, r as SUPPORT_EFFECT, s as lightIsInColorMode, t as getLightCurrentModeRgbColor } from './ha-more-info-dialog-dev.js';
import { s as stopPropagation } from './stop_propagation-dev.js';
import { s as supportsFeature } from './auth-dev.js';
import './ha-labeled-slider-dev.js';
import './ha-header-bar-dev.js';
import './mwc-tab-bar-dev.js';
import './ha-circular-progress-dev.js';
import './repeat-dev.js';

/**
 * Take input from [0, n] and return it as [0, 1]
 * @hidden
 */function bound01(n,max){if(isOnePointZero(n)){n='100%';}var isPercent=isPercentage(n);n=max===360?n:Math.min(max,Math.max(0,parseFloat(n)));// Automatically convert percentage into number
if(isPercent){n=parseInt(String(n*max),10)/100;}// Handle floating point rounding errors
if(Math.abs(n-max)<0.000001){return 1;}// Convert into [0, 1] range if it isn't already
if(max===360){// If n is a hue given in degrees,
// wrap around out-of-range values into [0, 360] range
// then convert into [0, 1].
n=(n<0?n%max+max:n%max)/parseFloat(String(max));}else {// If n not a hue given in degrees
// Convert into [0, 1] range if it isn't already.
n=n%max/parseFloat(String(max));}return n;}/**
 * Force a number between 0 and 1
 * @hidden
 */function clamp01(val){return Math.min(1,Math.max(0,val));}/**
 * Need to handle 1.0 as 100%, since once it is a number, there is no difference between it and 1
 * <http://stackoverflow.com/questions/7422072/javascript-how-to-detect-number-as-a-decimal-including-1-0>
 * @hidden
 */function isOnePointZero(n){return typeof n==='string'&&n.indexOf('.')!==-1&&parseFloat(n)===1;}/**
 * Check to see if string passed in is a percentage
 * @hidden
 */function isPercentage(n){return typeof n==='string'&&n.indexOf('%')!==-1;}/**
 * Return a valid alpha value [0,1] with all invalid values being set to 1
 * @hidden
 */function boundAlpha(a){a=parseFloat(a);if(isNaN(a)||a<0||a>1){a=1;}return a;}/**
 * Replace a decimal with it's percentage value
 * @hidden
 */function convertToPercentage(n){if(n<=1){return Number(n)*100+"%";}return n;}/**
 * Force a hex value to have 2 characters
 * @hidden
 */function pad2(c){return c.length===1?'0'+c:String(c);}

// <http://mjijackson.com/2008/02/rgb-to-hsl-and-rgb-to-hsv-color-model-conversion-algorithms-in-javascript>
/**
 * Handle bounds / percentage checking to conform to CSS color spec
 * <http://www.w3.org/TR/css3-color/>
 * *Assumes:* r, g, b in [0, 255] or [0, 1]
 * *Returns:* { r, g, b } in [0, 255]
 */function rgbToRgb(r,g,b){return {r:bound01(r,255)*255,g:bound01(g,255)*255,b:bound01(b,255)*255};}/**
 * Converts an RGB color value to HSL.
 * *Assumes:* r, g, and b are contained in [0, 255] or [0, 1]
 * *Returns:* { h, s, l } in [0,1]
 */function rgbToHsl(r,g,b){r=bound01(r,255);g=bound01(g,255);b=bound01(b,255);var max=Math.max(r,g,b);var min=Math.min(r,g,b);var h=0;var s=0;var l=(max+min)/2;if(max===min){s=0;h=0;// achromatic
}else {var d=max-min;s=l>0.5?d/(2-max-min):d/(max+min);switch(max){case r:h=(g-b)/d+(g<b?6:0);break;case g:h=(b-r)/d+2;break;case b:h=(r-g)/d+4;break;}h/=6;}return {h:h,s:s,l:l};}function hue2rgb(p,q,t){if(t<0){t+=1;}if(t>1){t-=1;}if(t<1/6){return p+(q-p)*(6*t);}if(t<1/2){return q;}if(t<2/3){return p+(q-p)*(2/3-t)*6;}return p;}/**
 * Converts an HSL color value to RGB.
 *
 * *Assumes:* h is contained in [0, 1] or [0, 360] and s and l are contained [0, 1] or [0, 100]
 * *Returns:* { r, g, b } in the set [0, 255]
 */function hslToRgb(h,s,l){var r;var g;var b;h=bound01(h,360);s=bound01(s,100);l=bound01(l,100);if(s===0){// achromatic
g=l;b=l;r=l;}else {var q=l<0.5?l*(1+s):l+s-l*s;var p=2*l-q;r=hue2rgb(p,q,h+1/3);g=hue2rgb(p,q,h);b=hue2rgb(p,q,h-1/3);}return {r:r*255,g:g*255,b:b*255};}/**
 * Converts an RGB color value to HSV
 *
 * *Assumes:* r, g, and b are contained in the set [0, 255] or [0, 1]
 * *Returns:* { h, s, v } in [0,1]
 */function rgbToHsv(r,g,b){r=bound01(r,255);g=bound01(g,255);b=bound01(b,255);var max=Math.max(r,g,b);var min=Math.min(r,g,b);var h=0;var v=max;var d=max-min;var s=max===0?0:d/max;if(max===min){h=0;// achromatic
}else {switch(max){case r:h=(g-b)/d+(g<b?6:0);break;case g:h=(b-r)/d+2;break;case b:h=(r-g)/d+4;break;}h/=6;}return {h:h,s:s,v:v};}/**
 * Converts an HSV color value to RGB.
 *
 * *Assumes:* h is contained in [0, 1] or [0, 360] and s and v are contained in [0, 1] or [0, 100]
 * *Returns:* { r, g, b } in the set [0, 255]
 */function hsvToRgb(h,s,v){h=bound01(h,360)*6;s=bound01(s,100);v=bound01(v,100);var i=Math.floor(h);var f=h-i;var p=v*(1-s);var q=v*(1-f*s);var t=v*(1-(1-f)*s);var mod=i%6;var r=[v,q,p,p,t,v][mod];var g=[t,v,v,q,p,p][mod];var b=[p,p,t,v,v,q][mod];return {r:r*255,g:g*255,b:b*255};}/**
 * Converts an RGB color to hex
 *
 * Assumes r, g, and b are contained in the set [0, 255]
 * Returns a 3 or 6 character hex
 */function rgbToHex(r,g,b,allow3Char){var hex=[pad2(Math.round(r).toString(16)),pad2(Math.round(g).toString(16)),pad2(Math.round(b).toString(16))];// Return a 3 character hex if possible
if(allow3Char&&hex[0].startsWith(hex[0].charAt(1))&&hex[1].startsWith(hex[1].charAt(1))&&hex[2].startsWith(hex[2].charAt(1))){return hex[0].charAt(0)+hex[1].charAt(0)+hex[2].charAt(0);}return hex.join('');}/**
 * Converts an RGBA color plus alpha transparency to hex
 *
 * Assumes r, g, b are contained in the set [0, 255] and
 * a in [0, 1]. Returns a 4 or 8 character rgba hex
 */ // eslint-disable-next-line max-params
function rgbaToHex(r,g,b,a,allow4Char){var hex=[pad2(Math.round(r).toString(16)),pad2(Math.round(g).toString(16)),pad2(Math.round(b).toString(16)),pad2(convertDecimalToHex(a))];// Return a 4 character hex if possible
if(allow4Char&&hex[0].startsWith(hex[0].charAt(1))&&hex[1].startsWith(hex[1].charAt(1))&&hex[2].startsWith(hex[2].charAt(1))&&hex[3].startsWith(hex[3].charAt(1))){return hex[0].charAt(0)+hex[1].charAt(0)+hex[2].charAt(0)+hex[3].charAt(0);}return hex.join('');}/** Converts a decimal to a hex value */function convertDecimalToHex(d){return Math.round(parseFloat(d)*255).toString(16);}/** Converts a hex value to a decimal */function convertHexToDecimal(h){return parseIntFromHex(h)/255;}/** Parse a base-16 hex value into a base-10 integer */function parseIntFromHex(val){return parseInt(val,16);}function numberInputToObject(color){return {r:color>>16,g:(color&0xff00)>>8,b:color&0xff};}

// https://github.com/bahamas10/css-color-names/blob/master/css-color-names.json
/**
 * @hidden
 */var names={aliceblue:'#f0f8ff',antiquewhite:'#faebd7',aqua:'#00ffff',aquamarine:'#7fffd4',azure:'#f0ffff',beige:'#f5f5dc',bisque:'#ffe4c4',black:'#000000',blanchedalmond:'#ffebcd',blue:'#0000ff',blueviolet:'#8a2be2',brown:'#a52a2a',burlywood:'#deb887',cadetblue:'#5f9ea0',chartreuse:'#7fff00',chocolate:'#d2691e',coral:'#ff7f50',cornflowerblue:'#6495ed',cornsilk:'#fff8dc',crimson:'#dc143c',cyan:'#00ffff',darkblue:'#00008b',darkcyan:'#008b8b',darkgoldenrod:'#b8860b',darkgray:'#a9a9a9',darkgreen:'#006400',darkgrey:'#a9a9a9',darkkhaki:'#bdb76b',darkmagenta:'#8b008b',darkolivegreen:'#556b2f',darkorange:'#ff8c00',darkorchid:'#9932cc',darkred:'#8b0000',darksalmon:'#e9967a',darkseagreen:'#8fbc8f',darkslateblue:'#483d8b',darkslategray:'#2f4f4f',darkslategrey:'#2f4f4f',darkturquoise:'#00ced1',darkviolet:'#9400d3',deeppink:'#ff1493',deepskyblue:'#00bfff',dimgray:'#696969',dimgrey:'#696969',dodgerblue:'#1e90ff',firebrick:'#b22222',floralwhite:'#fffaf0',forestgreen:'#228b22',fuchsia:'#ff00ff',gainsboro:'#dcdcdc',ghostwhite:'#f8f8ff',goldenrod:'#daa520',gold:'#ffd700',gray:'#808080',green:'#008000',greenyellow:'#adff2f',grey:'#808080',honeydew:'#f0fff0',hotpink:'#ff69b4',indianred:'#cd5c5c',indigo:'#4b0082',ivory:'#fffff0',khaki:'#f0e68c',lavenderblush:'#fff0f5',lavender:'#e6e6fa',lawngreen:'#7cfc00',lemonchiffon:'#fffacd',lightblue:'#add8e6',lightcoral:'#f08080',lightcyan:'#e0ffff',lightgoldenrodyellow:'#fafad2',lightgray:'#d3d3d3',lightgreen:'#90ee90',lightgrey:'#d3d3d3',lightpink:'#ffb6c1',lightsalmon:'#ffa07a',lightseagreen:'#20b2aa',lightskyblue:'#87cefa',lightslategray:'#778899',lightslategrey:'#778899',lightsteelblue:'#b0c4de',lightyellow:'#ffffe0',lime:'#00ff00',limegreen:'#32cd32',linen:'#faf0e6',magenta:'#ff00ff',maroon:'#800000',mediumaquamarine:'#66cdaa',mediumblue:'#0000cd',mediumorchid:'#ba55d3',mediumpurple:'#9370db',mediumseagreen:'#3cb371',mediumslateblue:'#7b68ee',mediumspringgreen:'#00fa9a',mediumturquoise:'#48d1cc',mediumvioletred:'#c71585',midnightblue:'#191970',mintcream:'#f5fffa',mistyrose:'#ffe4e1',moccasin:'#ffe4b5',navajowhite:'#ffdead',navy:'#000080',oldlace:'#fdf5e6',olive:'#808000',olivedrab:'#6b8e23',orange:'#ffa500',orangered:'#ff4500',orchid:'#da70d6',palegoldenrod:'#eee8aa',palegreen:'#98fb98',paleturquoise:'#afeeee',palevioletred:'#db7093',papayawhip:'#ffefd5',peachpuff:'#ffdab9',peru:'#cd853f',pink:'#ffc0cb',plum:'#dda0dd',powderblue:'#b0e0e6',purple:'#800080',rebeccapurple:'#663399',red:'#ff0000',rosybrown:'#bc8f8f',royalblue:'#4169e1',saddlebrown:'#8b4513',salmon:'#fa8072',sandybrown:'#f4a460',seagreen:'#2e8b57',seashell:'#fff5ee',sienna:'#a0522d',silver:'#c0c0c0',skyblue:'#87ceeb',slateblue:'#6a5acd',slategray:'#708090',slategrey:'#708090',snow:'#fffafa',springgreen:'#00ff7f',steelblue:'#4682b4',tan:'#d2b48c',teal:'#008080',thistle:'#d8bfd8',tomato:'#ff6347',turquoise:'#40e0d0',violet:'#ee82ee',wheat:'#f5deb3',white:'#ffffff',whitesmoke:'#f5f5f5',yellow:'#ffff00',yellowgreen:'#9acd32'};

/**
 * Given a string or object, convert that input to RGB
 *
 * Possible string inputs:
 * ```
 * "red"
 * "#f00" or "f00"
 * "#ff0000" or "ff0000"
 * "#ff000000" or "ff000000"
 * "rgb 255 0 0" or "rgb (255, 0, 0)"
 * "rgb 1.0 0 0" or "rgb (1, 0, 0)"
 * "rgba (255, 0, 0, 1)" or "rgba 255, 0, 0, 1"
 * "rgba (1.0, 0, 0, 1)" or "rgba 1.0, 0, 0, 1"
 * "hsl(0, 100%, 50%)" or "hsl 0 100% 50%"
 * "hsla(0, 100%, 50%, 1)" or "hsla 0 100% 50%, 1"
 * "hsv(0, 100%, 100%)" or "hsv 0 100% 100%"
 * ```
 */function inputToRGB(color){var rgb={r:0,g:0,b:0};var a=1;var s=null;var v=null;var l=null;var ok=false;var format=false;if(typeof color==='string'){color=stringInputToObject(color);}if(typeof color==='object'){if(isValidCSSUnit(color.r)&&isValidCSSUnit(color.g)&&isValidCSSUnit(color.b)){rgb=rgbToRgb(color.r,color.g,color.b);ok=true;format=String(color.r).substr(-1)==='%'?'prgb':'rgb';}else if(isValidCSSUnit(color.h)&&isValidCSSUnit(color.s)&&isValidCSSUnit(color.v)){s=convertToPercentage(color.s);v=convertToPercentage(color.v);rgb=hsvToRgb(color.h,s,v);ok=true;format='hsv';}else if(isValidCSSUnit(color.h)&&isValidCSSUnit(color.s)&&isValidCSSUnit(color.l)){s=convertToPercentage(color.s);l=convertToPercentage(color.l);rgb=hslToRgb(color.h,s,l);ok=true;format='hsl';}if(Object.prototype.hasOwnProperty.call(color,'a')){a=color.a;}}a=boundAlpha(a);return {ok:ok,format:color.format||format,r:Math.min(255,Math.max(rgb.r,0)),g:Math.min(255,Math.max(rgb.g,0)),b:Math.min(255,Math.max(rgb.b,0)),a:a};}// <http://www.w3.org/TR/css3-values/#integers>
var CSS_INTEGER='[-\\+]?\\d+%?';// <http://www.w3.org/TR/css3-values/#number-value>
var CSS_NUMBER='[-\\+]?\\d*\\.\\d+%?';// Allow positive/negative integer/number.  Don't capture the either/or, just the entire outcome.
var CSS_UNIT="(?:"+CSS_NUMBER+")|(?:"+CSS_INTEGER+")";// Actual matching.
// Parentheses and commas are optional, but not required.
// Whitespace can take the place of commas or opening paren
var PERMISSIVE_MATCH3="[\\s|\\(]+("+CSS_UNIT+")[,|\\s]+("+CSS_UNIT+")[,|\\s]+("+CSS_UNIT+")\\s*\\)?";var PERMISSIVE_MATCH4="[\\s|\\(]+("+CSS_UNIT+")[,|\\s]+("+CSS_UNIT+")[,|\\s]+("+CSS_UNIT+")[,|\\s]+("+CSS_UNIT+")\\s*\\)?";var matchers={CSS_UNIT:new RegExp(CSS_UNIT),rgb:new RegExp('rgb'+PERMISSIVE_MATCH3),rgba:new RegExp('rgba'+PERMISSIVE_MATCH4),hsl:new RegExp('hsl'+PERMISSIVE_MATCH3),hsla:new RegExp('hsla'+PERMISSIVE_MATCH4),hsv:new RegExp('hsv'+PERMISSIVE_MATCH3),hsva:new RegExp('hsva'+PERMISSIVE_MATCH4),hex3:/^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$/,hex6:/^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$/,hex4:/^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$/,hex8:/^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$/};/**
 * Permissive string parsing.  Take in a number of formats, and output an object
 * based on detected format.  Returns `{ r, g, b }` or `{ h, s, l }` or `{ h, s, v}`
 */function stringInputToObject(color){color=color.trim().toLowerCase();if(color.length===0){return false;}var named=false;if(names[color]){color=names[color];named=true;}else if(color==='transparent'){return {r:0,g:0,b:0,a:0,format:'name'};}// Try to match string input using regular expressions.
// Keep most of the number bounding out of this function - don't worry about [0,1] or [0,100] or [0,360]
// Just return an object and let the conversion functions handle that.
// This way the result will be the same whether the tinycolor is initialized with string or object.
var match=matchers.rgb.exec(color);if(match){return {r:match[1],g:match[2],b:match[3]};}match=matchers.rgba.exec(color);if(match){return {r:match[1],g:match[2],b:match[3],a:match[4]};}match=matchers.hsl.exec(color);if(match){return {h:match[1],s:match[2],l:match[3]};}match=matchers.hsla.exec(color);if(match){return {h:match[1],s:match[2],l:match[3],a:match[4]};}match=matchers.hsv.exec(color);if(match){return {h:match[1],s:match[2],v:match[3]};}match=matchers.hsva.exec(color);if(match){return {h:match[1],s:match[2],v:match[3],a:match[4]};}match=matchers.hex8.exec(color);if(match){return {r:parseIntFromHex(match[1]),g:parseIntFromHex(match[2]),b:parseIntFromHex(match[3]),a:convertHexToDecimal(match[4]),format:named?'name':'hex8'};}match=matchers.hex6.exec(color);if(match){return {r:parseIntFromHex(match[1]),g:parseIntFromHex(match[2]),b:parseIntFromHex(match[3]),format:named?'name':'hex'};}match=matchers.hex4.exec(color);if(match){return {r:parseIntFromHex(match[1]+match[1]),g:parseIntFromHex(match[2]+match[2]),b:parseIntFromHex(match[3]+match[3]),a:convertHexToDecimal(match[4]+match[4]),format:named?'name':'hex8'};}match=matchers.hex3.exec(color);if(match){return {r:parseIntFromHex(match[1]+match[1]),g:parseIntFromHex(match[2]+match[2]),b:parseIntFromHex(match[3]+match[3]),format:named?'name':'hex'};}return false;}/**
 * Check to see if it looks like a CSS unit
 * (see `matchers` above for definition).
 */function isValidCSSUnit(color){return Boolean(matchers.CSS_UNIT.exec(String(color)));}

var TinyColor=/** @class */function(){function TinyColor(color,opts){if(color===void 0){color='';}if(opts===void 0){opts={};}var _a;// If input is already a tinycolor, return itself
if(color instanceof TinyColor){// eslint-disable-next-line no-constructor-return
return color;}if(typeof color==='number'){color=numberInputToObject(color);}this.originalInput=color;var rgb=inputToRGB(color);this.originalInput=color;this.r=rgb.r;this.g=rgb.g;this.b=rgb.b;this.a=rgb.a;this.roundA=Math.round(100*this.a)/100;this.format=(_a=opts.format)!==null&&_a!==void 0?_a:rgb.format;this.gradientType=opts.gradientType;// Don't let the range of [0,255] come back in [0,1].
// Potentially lose a little bit of precision here, but will fix issues where
// .5 gets interpreted as half of the total, instead of half of 1
// If it was supposed to be 128, this was already taken care of by `inputToRgb`
if(this.r<1){this.r=Math.round(this.r);}if(this.g<1){this.g=Math.round(this.g);}if(this.b<1){this.b=Math.round(this.b);}this.isValid=rgb.ok;}TinyColor.prototype.isDark=function(){return this.getBrightness()<128;};TinyColor.prototype.isLight=function(){return !this.isDark();};/**
     * Returns the perceived brightness of the color, from 0-255.
     */TinyColor.prototype.getBrightness=function(){// http://www.w3.org/TR/AERT#color-contrast
var rgb=this.toRgb();return (rgb.r*299+rgb.g*587+rgb.b*114)/1000;};/**
     * Returns the perceived luminance of a color, from 0-1.
     */TinyColor.prototype.getLuminance=function(){// http://www.w3.org/TR/2008/REC-WCAG20-20081211/#relativeluminancedef
var rgb=this.toRgb();var R;var G;var B;var RsRGB=rgb.r/255;var GsRGB=rgb.g/255;var BsRGB=rgb.b/255;if(RsRGB<=0.03928){R=RsRGB/12.92;}else {// eslint-disable-next-line prefer-exponentiation-operator
R=Math.pow((RsRGB+0.055)/1.055,2.4);}if(GsRGB<=0.03928){G=GsRGB/12.92;}else {// eslint-disable-next-line prefer-exponentiation-operator
G=Math.pow((GsRGB+0.055)/1.055,2.4);}if(BsRGB<=0.03928){B=BsRGB/12.92;}else {// eslint-disable-next-line prefer-exponentiation-operator
B=Math.pow((BsRGB+0.055)/1.055,2.4);}return 0.2126*R+0.7152*G+0.0722*B;};/**
     * Returns the alpha value of a color, from 0-1.
     */TinyColor.prototype.getAlpha=function(){return this.a;};/**
     * Sets the alpha value on the current color.
     *
     * @param alpha - The new alpha value. The accepted range is 0-1.
     */TinyColor.prototype.setAlpha=function(alpha){this.a=boundAlpha(alpha);this.roundA=Math.round(100*this.a)/100;return this;};/**
     * Returns the object as a HSVA object.
     */TinyColor.prototype.toHsv=function(){var hsv=rgbToHsv(this.r,this.g,this.b);return {h:hsv.h*360,s:hsv.s,v:hsv.v,a:this.a};};/**
     * Returns the hsva values interpolated into a string with the following format:
     * "hsva(xxx, xxx, xxx, xx)".
     */TinyColor.prototype.toHsvString=function(){var hsv=rgbToHsv(this.r,this.g,this.b);var h=Math.round(hsv.h*360);var s=Math.round(hsv.s*100);var v=Math.round(hsv.v*100);return this.a===1?"hsv("+h+", "+s+"%, "+v+"%)":"hsva("+h+", "+s+"%, "+v+"%, "+this.roundA+")";};/**
     * Returns the object as a HSLA object.
     */TinyColor.prototype.toHsl=function(){var hsl=rgbToHsl(this.r,this.g,this.b);return {h:hsl.h*360,s:hsl.s,l:hsl.l,a:this.a};};/**
     * Returns the hsla values interpolated into a string with the following format:
     * "hsla(xxx, xxx, xxx, xx)".
     */TinyColor.prototype.toHslString=function(){var hsl=rgbToHsl(this.r,this.g,this.b);var h=Math.round(hsl.h*360);var s=Math.round(hsl.s*100);var l=Math.round(hsl.l*100);return this.a===1?"hsl("+h+", "+s+"%, "+l+"%)":"hsla("+h+", "+s+"%, "+l+"%, "+this.roundA+")";};/**
     * Returns the hex value of the color.
     * @param allow3Char will shorten hex value to 3 char if possible
     */TinyColor.prototype.toHex=function(allow3Char){if(allow3Char===void 0){allow3Char=false;}return rgbToHex(this.r,this.g,this.b,allow3Char);};/**
     * Returns the hex value of the color -with a # appened.
     * @param allow3Char will shorten hex value to 3 char if possible
     */TinyColor.prototype.toHexString=function(allow3Char){if(allow3Char===void 0){allow3Char=false;}return '#'+this.toHex(allow3Char);};/**
     * Returns the hex 8 value of the color.
     * @param allow4Char will shorten hex value to 4 char if possible
     */TinyColor.prototype.toHex8=function(allow4Char){if(allow4Char===void 0){allow4Char=false;}return rgbaToHex(this.r,this.g,this.b,this.a,allow4Char);};/**
     * Returns the hex 8 value of the color -with a # appened.
     * @param allow4Char will shorten hex value to 4 char if possible
     */TinyColor.prototype.toHex8String=function(allow4Char){if(allow4Char===void 0){allow4Char=false;}return '#'+this.toHex8(allow4Char);};/**
     * Returns the object as a RGBA object.
     */TinyColor.prototype.toRgb=function(){return {r:Math.round(this.r),g:Math.round(this.g),b:Math.round(this.b),a:this.a};};/**
     * Returns the RGBA values interpolated into a string with the following format:
     * "RGBA(xxx, xxx, xxx, xx)".
     */TinyColor.prototype.toRgbString=function(){var r=Math.round(this.r);var g=Math.round(this.g);var b=Math.round(this.b);return this.a===1?"rgb("+r+", "+g+", "+b+")":"rgba("+r+", "+g+", "+b+", "+this.roundA+")";};/**
     * Returns the object as a RGBA object.
     */TinyColor.prototype.toPercentageRgb=function(){var fmt=function(x){return Math.round(bound01(x,255)*100)+"%";};return {r:fmt(this.r),g:fmt(this.g),b:fmt(this.b),a:this.a};};/**
     * Returns the RGBA relative values interpolated into a string
     */TinyColor.prototype.toPercentageRgbString=function(){var rnd=function(x){return Math.round(bound01(x,255)*100);};return this.a===1?"rgb("+rnd(this.r)+"%, "+rnd(this.g)+"%, "+rnd(this.b)+"%)":"rgba("+rnd(this.r)+"%, "+rnd(this.g)+"%, "+rnd(this.b)+"%, "+this.roundA+")";};/**
     * The 'real' name of the color -if there is one.
     */TinyColor.prototype.toName=function(){if(this.a===0){return 'transparent';}if(this.a<1){return false;}var hex='#'+rgbToHex(this.r,this.g,this.b,false);for(var _i=0,_a=Object.entries(names);_i<_a.length;_i++){var _b=_a[_i],key=_b[0],value=_b[1];if(hex===value){return key;}}return false;};TinyColor.prototype.toString=function(format){var formatSet=Boolean(format);format=format!==null&&format!==void 0?format:this.format;var formattedString=false;var hasAlpha=this.a<1&&this.a>=0;var needsAlphaFormat=!formatSet&&hasAlpha&&(format.startsWith('hex')||format==='name');if(needsAlphaFormat){// Special case for "transparent", all other non-alpha formats
// will return rgba when there is transparency.
if(format==='name'&&this.a===0){return this.toName();}return this.toRgbString();}if(format==='rgb'){formattedString=this.toRgbString();}if(format==='prgb'){formattedString=this.toPercentageRgbString();}if(format==='hex'||format==='hex6'){formattedString=this.toHexString();}if(format==='hex3'){formattedString=this.toHexString(true);}if(format==='hex4'){formattedString=this.toHex8String(true);}if(format==='hex8'){formattedString=this.toHex8String();}if(format==='name'){formattedString=this.toName();}if(format==='hsl'){formattedString=this.toHslString();}if(format==='hsv'){formattedString=this.toHsvString();}return formattedString||this.toHexString();};TinyColor.prototype.toNumber=function(){return (Math.round(this.r)<<16)+(Math.round(this.g)<<8)+Math.round(this.b);};TinyColor.prototype.clone=function(){return new TinyColor(this.toString());};/**
     * Lighten the color a given amount. Providing 100 will always return white.
     * @param amount - valid between 1-100
     */TinyColor.prototype.lighten=function(amount){if(amount===void 0){amount=10;}var hsl=this.toHsl();hsl.l+=amount/100;hsl.l=clamp01(hsl.l);return new TinyColor(hsl);};/**
     * Brighten the color a given amount, from 0 to 100.
     * @param amount - valid between 1-100
     */TinyColor.prototype.brighten=function(amount){if(amount===void 0){amount=10;}var rgb=this.toRgb();rgb.r=Math.max(0,Math.min(255,rgb.r-Math.round(255*-(amount/100))));rgb.g=Math.max(0,Math.min(255,rgb.g-Math.round(255*-(amount/100))));rgb.b=Math.max(0,Math.min(255,rgb.b-Math.round(255*-(amount/100))));return new TinyColor(rgb);};/**
     * Darken the color a given amount, from 0 to 100.
     * Providing 100 will always return black.
     * @param amount - valid between 1-100
     */TinyColor.prototype.darken=function(amount){if(amount===void 0){amount=10;}var hsl=this.toHsl();hsl.l-=amount/100;hsl.l=clamp01(hsl.l);return new TinyColor(hsl);};/**
     * Mix the color with pure white, from 0 to 100.
     * Providing 0 will do nothing, providing 100 will always return white.
     * @param amount - valid between 1-100
     */TinyColor.prototype.tint=function(amount){if(amount===void 0){amount=10;}return this.mix('white',amount);};/**
     * Mix the color with pure black, from 0 to 100.
     * Providing 0 will do nothing, providing 100 will always return black.
     * @param amount - valid between 1-100
     */TinyColor.prototype.shade=function(amount){if(amount===void 0){amount=10;}return this.mix('black',amount);};/**
     * Desaturate the color a given amount, from 0 to 100.
     * Providing 100 will is the same as calling greyscale
     * @param amount - valid between 1-100
     */TinyColor.prototype.desaturate=function(amount){if(amount===void 0){amount=10;}var hsl=this.toHsl();hsl.s-=amount/100;hsl.s=clamp01(hsl.s);return new TinyColor(hsl);};/**
     * Saturate the color a given amount, from 0 to 100.
     * @param amount - valid between 1-100
     */TinyColor.prototype.saturate=function(amount){if(amount===void 0){amount=10;}var hsl=this.toHsl();hsl.s+=amount/100;hsl.s=clamp01(hsl.s);return new TinyColor(hsl);};/**
     * Completely desaturates a color into greyscale.
     * Same as calling `desaturate(100)`
     */TinyColor.prototype.greyscale=function(){return this.desaturate(100);};/**
     * Spin takes a positive or negative amount within [-360, 360] indicating the change of hue.
     * Values outside of this range will be wrapped into this range.
     */TinyColor.prototype.spin=function(amount){var hsl=this.toHsl();var hue=(hsl.h+amount)%360;hsl.h=hue<0?360+hue:hue;return new TinyColor(hsl);};/**
     * Mix the current color a given amount with another color, from 0 to 100.
     * 0 means no mixing (return current color).
     */TinyColor.prototype.mix=function(color,amount){if(amount===void 0){amount=50;}var rgb1=this.toRgb();var rgb2=new TinyColor(color).toRgb();var p=amount/100;var rgba={r:(rgb2.r-rgb1.r)*p+rgb1.r,g:(rgb2.g-rgb1.g)*p+rgb1.g,b:(rgb2.b-rgb1.b)*p+rgb1.b,a:(rgb2.a-rgb1.a)*p+rgb1.a};return new TinyColor(rgba);};TinyColor.prototype.analogous=function(results,slices){if(results===void 0){results=6;}if(slices===void 0){slices=30;}var hsl=this.toHsl();var part=360/slices;var ret=[this];for(hsl.h=(hsl.h-(part*results>>1)+720)%360;--results;){hsl.h=(hsl.h+part)%360;ret.push(new TinyColor(hsl));}return ret;};/**
     * taken from https://github.com/infusion/jQuery-xcolor/blob/master/jquery.xcolor.js
     */TinyColor.prototype.complement=function(){var hsl=this.toHsl();hsl.h=(hsl.h+180)%360;return new TinyColor(hsl);};TinyColor.prototype.monochromatic=function(results){if(results===void 0){results=6;}var hsv=this.toHsv();var h=hsv.h;var s=hsv.s;var v=hsv.v;var res=[];var modification=1/results;while(results--){res.push(new TinyColor({h:h,s:s,v:v}));v=(v+modification)%1;}return res;};TinyColor.prototype.splitcomplement=function(){var hsl=this.toHsl();var h=hsl.h;return [this,new TinyColor({h:(h+72)%360,s:hsl.s,l:hsl.l}),new TinyColor({h:(h+216)%360,s:hsl.s,l:hsl.l})];};/**
     * Compute how the color would appear on a background
     */TinyColor.prototype.onBackground=function(background){var fg=this.toRgb();var bg=new TinyColor(background).toRgb();return new TinyColor({r:bg.r+(fg.r-bg.r)*fg.a,g:bg.g+(fg.g-bg.g)*fg.a,b:bg.b+(fg.b-bg.b)*fg.a});};/**
     * Alias for `polyad(3)`
     */TinyColor.prototype.triad=function(){return this.polyad(3);};/**
     * Alias for `polyad(4)`
     */TinyColor.prototype.tetrad=function(){return this.polyad(4);};/**
     * Get polyad colors, like (for 1, 2, 3, 4, 5, 6, 7, 8, etc...)
     * monad, dyad, triad, tetrad, pentad, hexad, heptad, octad, etc...
     */TinyColor.prototype.polyad=function(n){var hsl=this.toHsl();var h=hsl.h;var result=[this];var increment=360/n;for(var i=1;i<n;i++){result.push(new TinyColor({h:(h+i*increment)%360,s:hsl.s,l:hsl.l}));}return result;};/**
     * compare color vs current color
     */TinyColor.prototype.equals=function(color){return this.toRgbString()===new TinyColor(color).toRgbString();};return TinyColor;}();function tinycolor(color,opts){if(color===void 0){color='';}if(opts===void 0){opts={};}return new TinyColor(color,opts);}

/**
 * Color-picker custom element
 *
 * @appliesMixin EventsMixin
 */class HaColorPicker extends EventsMixin(PolymerElement){static get template(){return html`
      <style>
        :host {
          user-select: none;
          -webkit-user-select: none;
        }

        #canvas {
          position: relative;
          width: 100%;
          max-width: 330px;
        }
        #canvas > * {
          display: block;
        }
        #interactionLayer {
          color: white;
          position: absolute;
          cursor: crosshair;
          width: 100%;
          height: 100%;
          overflow: visible;
        }
        #backgroundLayer {
          width: 100%;
          overflow: visible;
          --wheel-bordercolor: var(--ha-color-picker-wheel-bordercolor, white);
          --wheel-borderwidth: var(--ha-color-picker-wheel-borderwidth, 3);
          --wheel-shadow: var(
            --ha-color-picker-wheel-shadow,
            rgb(15, 15, 15) 10px 5px 5px 0px
          );
        }

        #marker {
          fill: currentColor;
          stroke: var(--ha-color-picker-marker-bordercolor, white);
          stroke-width: var(--ha-color-picker-marker-borderwidth, 3);
          filter: url(#marker-shadow);
        }
        .dragging #marker {
        }

        #colorTooltip {
          display: none;
          fill: currentColor;
          stroke: var(--ha-color-picker-tooltip-bordercolor, white);
          stroke-width: var(--ha-color-picker-tooltip-borderwidth, 3);
        }

        .touch.dragging #colorTooltip {
          display: inherit;
        }
      </style>
      <div id="canvas">
        <svg id="interactionLayer">
          <defs>
            <filter
              id="marker-shadow"
              x="-50%"
              y="-50%"
              width="200%"
              height="200%"
              filterUnits="objectBoundingBox"
            >
              <feOffset
                result="offOut"
                in="SourceAlpha"
                dx="2"
                dy="2"
              ></feOffset>
              <feGaussianBlur
                result="blurOut"
                in="offOut"
                stdDeviation="2"
              ></feGaussianBlur>
              <feComponentTransfer in="blurOut" result="alphaOut">
                <feFuncA type="linear" slope="0.3"></feFuncA>
              </feComponentTransfer>
              <feBlend
                in="SourceGraphic"
                in2="alphaOut"
                mode="normal"
              ></feBlend>
            </filter>
          </defs>
        </svg>
        <canvas id="backgroundLayer"></canvas>
      </div>
    `;}static get properties(){return {hsColor:{type:Object},// use these properties to update the state via attributes
desiredHsColor:{type:Object,observer:"applyHsColor"},// use these properties to update the state via attributes
desiredRgbColor:{type:Object,observer:"applyRgbColor"},// width, height and radius apply to the coordinates of
// of the canvas.
// border width are relative to these numbers
// the onscreen displayed size should be controlled with css
// and should be the same or smaller
width:{type:Number,value:500},height:{type:Number,value:500},radius:{type:Number,value:225},// the amount segments for the hue
// 0 = continuous gradient
// other than 0 gives 'pie-pieces'
hueSegments:{type:Number,value:0,observer:"segmentationChange"},// the amount segments for the hue
// 0 = continuous gradient
// 1 = only fully saturated
// > 1 = segments from white to fully saturated
saturationSegments:{type:Number,value:0,observer:"segmentationChange"},// set to true to make the segments purely esthetical
// this allows selection off all collors, also
// interpolated between the segments
ignoreSegments:{type:Boolean,value:false},// throttle te amount of 'colorselected' events fired
// value is timeout in milliseconds
throttle:{type:Number,value:500}};}ready(){super.ready();this.setupLayers();this.drawColorWheel();this.drawMarker();if(this.desiredHsColor){this.applyHsColor(this.desiredHsColor);}if(this.desiredRgbColor){this.applyRgbColor(this.desiredRgbColor);}this.interactionLayer.addEventListener("mousedown",ev=>this.onMouseDown(ev));this.interactionLayer.addEventListener("touchstart",ev=>this.onTouchStart(ev));}// converts browser coordinates to canvas canvas coordinates
// origin is wheel center
// returns {x: X, y: Y} object
convertToCanvasCoordinates(clientX,clientY){const svgPoint=this.interactionLayer.createSVGPoint();svgPoint.x=clientX;svgPoint.y=clientY;const cc=svgPoint.matrixTransform(this.interactionLayer.getScreenCTM().inverse());return {x:cc.x,y:cc.y};}// Mouse events
onMouseDown(ev){const cc=this.convertToCanvasCoordinates(ev.clientX,ev.clientY);// return if we're not on the wheel
if(!this.isInWheel(cc.x,cc.y)){return;}// a mousedown in wheel is always a color select action
this.onMouseSelect(ev);// allow dragging
this.canvas.classList.add("mouse","dragging");this.addEventListener("mousemove",this.onMouseSelect);this.addEventListener("mouseup",this.onMouseUp);}onMouseUp(){this.canvas.classList.remove("mouse","dragging");this.removeEventListener("mousemove",this.onMouseSelect);}onMouseSelect(ev){requestAnimationFrame(()=>this.processUserSelect(ev));}// Touch events
onTouchStart(ev){const touch=ev.changedTouches[0];const cc=this.convertToCanvasCoordinates(touch.clientX,touch.clientY);// return if we're not on the wheel
if(!this.isInWheel(cc.x,cc.y)){return;}if(ev.target===this.marker){// drag marker
ev.preventDefault();this.canvas.classList.add("touch","dragging");this.addEventListener("touchmove",this.onTouchSelect);this.addEventListener("touchend",this.onTouchEnd);return;}// don't fire color selection immediately,
// wait for touchend and invalidate when we scroll
this.tapBecameScroll=false;this.addEventListener("touchend",this.onTap);this.addEventListener("touchmove",()=>{this.tapBecameScroll=true;},{passive:true});}onTap(ev){if(this.tapBecameScroll){return;}ev.preventDefault();this.onTouchSelect(ev);}onTouchEnd(){this.canvas.classList.remove("touch","dragging");this.removeEventListener("touchmove",this.onTouchSelect);}onTouchSelect(ev){requestAnimationFrame(()=>this.processUserSelect(ev.changedTouches[0]));}/*
   * General event/selection handling
   */ // Process user input to color
processUserSelect(ev){const canvasXY=this.convertToCanvasCoordinates(ev.clientX,ev.clientY);const hs=this.getColor(canvasXY.x,canvasXY.y);let rgb;if(!this.isInWheel(canvasXY.x,canvasXY.y)){const[r,g,b]=hs2rgb([hs.h,hs.s]);rgb={r,g,b};}else {rgb=this.getRgbColor(canvasXY.x,canvasXY.y);}this.onColorSelect(hs,rgb);}// apply color to marker position and canvas
onColorSelect(hs,rgb){this.setMarkerOnColor(hs);// marker always follows mouse 'raw' hs value (= mouse position)
if(!this.ignoreSegments){// apply segments if needed
hs=this.applySegmentFilter(hs);}// always apply the new color to the interface / canvas
this.applyColorToCanvas(hs);// throttling is applied to updating the exposed colors (properties)
// and firing of events
if(this.colorSelectIsThrottled){// make sure we apply the last selected color
// eventually after throttle limit has passed
clearTimeout(this.ensureFinalSelect);this.ensureFinalSelect=setTimeout(()=>{this.fireColorSelected(hs,rgb);// do it for the final time
},this.throttle);return;}this.fireColorSelected(hs,rgb);// do it
this.colorSelectIsThrottled=true;setTimeout(()=>{this.colorSelectIsThrottled=false;},this.throttle);}// set color values and fire colorselected event
fireColorSelected(hs,rgb){this.hsColor=hs;this.fire("colorselected",{hs,rgb});}/*
   * Interface updating
   */ // set marker position to the given color
setMarkerOnColor(hs){if(!this.marker||!this.tooltip){return;}const dist=hs.s*this.radius;const theta=(hs.h-180)/180*Math.PI;const markerdX=-dist*Math.cos(theta);const markerdY=-dist*Math.sin(theta);const translateString=`translate(${markerdX},${markerdY})`;this.marker.setAttribute("transform",translateString);this.tooltip.setAttribute("transform",translateString);}// apply given color to interface elements
applyColorToCanvas(hs){if(!this.interactionLayer){return;}// we're not really converting hs to hsl here, but we keep it cheap
// setting the color on the interactionLayer, the svg elements can inherit
this.interactionLayer.style.color=`hsl(${hs.h}, 100%, ${100-hs.s*50}%)`;}applyHsColor(hs){// do nothing is we already have the same color
if(this.hsColor&&this.hsColor.h===hs.h&&this.hsColor.s===hs.s){return;}this.setMarkerOnColor(hs);// marker is always set on 'raw' hs position
if(!this.ignoreSegments){// apply segments if needed
hs=this.applySegmentFilter(hs);}this.hsColor=hs;// always apply the new color to the interface / canvas
this.applyColorToCanvas(hs);}applyRgbColor(rgb){const[h,s]=rgb2hs(rgb);this.applyHsColor({h,s});}/*
   * input processing helpers
   */ // get angle (degrees)
getAngle(dX,dY){const theta=Math.atan2(-dY,-dX);// radians from the left edge, clockwise = positive
const angle=theta/Math.PI*180+180;// degrees, clockwise from right
return angle;}// returns true when coordinates are in the colorwheel
isInWheel(x,y){return this.getDistance(x,y)<=1;}// returns distance from wheel center, 0 = center, 1 = edge, >1 = outside
getDistance(dX,dY){return Math.sqrt(dX*dX+dY*dY)/this.radius;}/*
   * Getting colors
   */getColor(x,y){const hue=this.getAngle(x,y);// degrees, clockwise from right
const relativeDistance=this.getDistance(x,y);// edge of radius = 1
const sat=Math.min(relativeDistance,1);// Distance from center
return {h:hue,s:sat};}getRgbColor(x,y){// get current pixel
const imageData=this.backgroundLayer.getContext("2d").getImageData(x+250,y+250,1,1);const pixel=imageData.data;return {r:pixel[0],g:pixel[1],b:pixel[2]};}applySegmentFilter(hs){// apply hue segment steps
if(this.hueSegments){const angleStep=360/this.hueSegments;const halfAngleStep=angleStep/2;hs.h-=halfAngleStep;// take the 'centered segemnts' into account
if(hs.h<0){hs.h+=360;}// don't end up below 0
const rest=hs.h%angleStep;hs.h-=rest-angleStep;}// apply saturation segment steps
if(this.saturationSegments){if(this.saturationSegments===1){hs.s=1;}else {const segmentSize=1/this.saturationSegments;const saturationStep=1/(this.saturationSegments-1);const calculatedSat=Math.floor(hs.s/segmentSize)*saturationStep;hs.s=Math.min(calculatedSat,1);}}return hs;}/*
   * Drawing related stuff
   */setupLayers(){this.canvas=this.$.canvas;this.backgroundLayer=this.$.backgroundLayer;this.interactionLayer=this.$.interactionLayer;// coordinate origin position (center of the wheel)
this.originX=this.width/2;this.originY=this.originX;// synchronise width/height coordinates
this.backgroundLayer.width=this.width;this.backgroundLayer.height=this.height;this.interactionLayer.setAttribute("viewBox",`${-this.originX} ${-this.originY} ${this.width} ${this.height}`);}drawColorWheel(){/*
     *  Setting up all paremeters
     */let shadowColor;let shadowOffsetX;let shadowOffsetY;let shadowBlur;const context=this.backgroundLayer.getContext("2d");// postioning and sizing
const cX=this.originX;const cY=this.originY;const radius=this.radius;const counterClockwise=false;// styling of the wheel
const wheelStyle=window.getComputedStyle(this.backgroundLayer,null);const borderWidth=parseInt(wheelStyle.getPropertyValue("--wheel-borderwidth"),10);const borderColor=wheelStyle.getPropertyValue("--wheel-bordercolor").trim();const wheelShadow=wheelStyle.getPropertyValue("--wheel-shadow").trim();// extract shadow properties from CSS variable
// the shadow should be defined as: "10px 5px 5px 0px COLOR"
if(wheelShadow!=="none"){const values=wheelShadow.split("px ");shadowColor=values.pop();shadowOffsetX=parseInt(values[0],10);shadowOffsetY=parseInt(values[1],10);shadowBlur=parseInt(values[2],10)||0;}const borderRadius=radius+borderWidth/2;const wheelRadius=radius;const shadowRadius=radius+borderWidth;/*
     *  Drawing functions
     */function drawCircle(hueSegments,saturationSegments){hueSegments=hueSegments||360;// reset 0 segments to 360
const angleStep=360/hueSegments;const halfAngleStep=angleStep/2;// center segments on color
for(let angle=0;angle<=360;angle+=angleStep){const startAngle=(angle-halfAngleStep)*(Math.PI/180);const endAngle=(angle+halfAngleStep+1)*(Math.PI/180);context.beginPath();context.moveTo(cX,cY);context.arc(cX,cY,wheelRadius,startAngle,endAngle,counterClockwise);context.closePath();// gradient
const gradient=context.createRadialGradient(cX,cY,0,cX,cY,wheelRadius);let lightness=100;// first gradient stop
gradient.addColorStop(0,`hsl(${angle}, 100%, ${lightness}%)`);// segment gradient stops
if(saturationSegments>0){const ratioStep=1/saturationSegments;let ratio=0;for(let stop=1;stop<saturationSegments;stop+=1){const prevLighness=lightness;ratio=stop*ratioStep;lightness=100-50*ratio;gradient.addColorStop(ratio,`hsl(${angle}, 100%, ${prevLighness}%)`);gradient.addColorStop(ratio,`hsl(${angle}, 100%, ${lightness}%)`);}gradient.addColorStop(ratio,`hsl(${angle}, 100%, 50%)`);}// last gradient stop
gradient.addColorStop(1,`hsl(${angle}, 100%, 50%)`);context.fillStyle=gradient;context.fill();}}function drawShadow(){context.save();context.beginPath();context.arc(cX,cY,shadowRadius,0,2*Math.PI,false);context.shadowColor=shadowColor;context.shadowOffsetX=shadowOffsetX;context.shadowOffsetY=shadowOffsetY;context.shadowBlur=shadowBlur;context.fillStyle="white";context.fill();context.restore();}function drawBorder(){context.beginPath();context.arc(cX,cY,borderRadius,0,2*Math.PI,false);context.lineWidth=borderWidth;context.strokeStyle=borderColor;context.stroke();}/*
     *   Call the drawing functions
     *   draws the shadow, wheel and border
     */if(wheelStyle.shadow!=="none"){drawShadow();}drawCircle(this.hueSegments,this.saturationSegments);if(borderWidth>0){drawBorder();}}/*
   *   Draw the (draggable) marker and tooltip
   *   on the interactionLayer)
   */drawMarker(){const svgElement=this.interactionLayer;const markerradius=this.radius*0.08;const tooltipradius=this.radius*0.15;const TooltipOffsetY=-(tooltipradius*3);const TooltipOffsetX=0;svgElement.marker=document.createElementNS("http://www.w3.org/2000/svg","circle");svgElement.marker.setAttribute("id","marker");svgElement.marker.setAttribute("r",markerradius);this.marker=svgElement.marker;svgElement.appendChild(svgElement.marker);svgElement.tooltip=document.createElementNS("http://www.w3.org/2000/svg","circle");svgElement.tooltip.setAttribute("id","colorTooltip");svgElement.tooltip.setAttribute("r",tooltipradius);svgElement.tooltip.setAttribute("cx",TooltipOffsetX);svgElement.tooltip.setAttribute("cy",TooltipOffsetY);this.tooltip=svgElement.tooltip;svgElement.appendChild(svgElement.tooltip);}segmentationChange(){if(this.backgroundLayer){this.drawColorWheel();}}}customElements.define("ha-color-picker",HaColorPicker);

function trigger(element,type){if(!element||!type){return;}// Create and dispatch the event
const event=new Event(type,{bubbles:true});// Dispatch the event
element.dispatchEvent(event);}function getDecimalPlaces(value){const match=`${value}`.match(/(?:\.(\d+))?(?:[eE]([+-]?\d+))?$/);if(!match){return 0;}return Math.max(0,// Number of digits right of decimal point.
(match[1]?match[1].length:0)-(// Adjust for scientific notation.
match[2]?+match[2]:0));}function round(number,step){if(step<1){const places=getDecimalPlaces(step);return parseFloat(number.toFixed(places));}return Math.round(number/step)*step;}_decorate([n("more-info-light")],function(_initialize,_LitElement){class MoreInfoLight extends _LitElement{constructor(...args){super(...args);_initialize(this);}}return {F:MoreInfoLight,d:[{kind:"field",decorators:[e({attribute:false})],key:"hass",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"stateObj",value:void 0},{kind:"field",decorators:[t()],key:"_brightnessSliderValue",value(){return 0;}},{kind:"field",decorators:[t()],key:"_ctSliderValue",value:void 0},{kind:"field",decorators:[t()],key:"_cwSliderValue",value:void 0},{kind:"field",decorators:[t()],key:"_wwSliderValue",value:void 0},{kind:"field",decorators:[t()],key:"_wvSliderValue",value:void 0},{kind:"field",decorators:[t()],key:"_colorBrightnessSliderValue",value:void 0},{kind:"field",decorators:[t()],key:"_brightnessAdjusted",value:void 0},{kind:"field",decorators:[t()],key:"_hueSegments",value(){return 24;}},{kind:"field",decorators:[t()],key:"_saturationSegments",value(){return 8;}},{kind:"field",decorators:[t()],key:"_colorPickerColor",value:void 0},{kind:"field",decorators:[t()],key:"_mode",value:void 0},{kind:"field",decorators:[e({attribute:false})],key:"actionRows",value(){return [];}},{kind:"field",decorators:[e({attribute:false})],key:"settingsOn",value(){return true;}},{kind:"method",key:"get",value:function get(event){const confthumbWidth=0;const input=event.target;const touch=event.changedTouches[0];const min=parseFloat(input.getAttribute("min"))||0;const max=parseFloat(input.getAttribute("max"))||100;const step=parseFloat(input.getAttribute("step"))||1;const delta=max-min;// Calculate percentage
let percent;const clientRect=input.getBoundingClientRect();const thumbWidth=100/clientRect.width*(confthumbWidth/2)/100;// Determine left percentage
{percent=100-100/clientRect.height*(touch.clientY-clientRect.top);}// Don't allow outside bounds
if(percent<0){percent=0;}else if(percent>100){percent=100;}// Factor in the thumb offset
if(percent<50){percent-=(100-percent*2)*thumbWidth;}else if(percent>50){percent+=(percent-50)*2*thumbWidth;}// Find the closest step to the mouse position
return min+round(delta*(percent/100),step);}},{kind:"method",key:"set",value:function set(event){// Prevent text highlight on iOS
event.preventDefault();// Set value
// eslint-disable-next-line no-param-reassign
event.target.value=this.get(event);// Trigger event
trigger(event.target,event.type==="touchend"?"change":"input");}},{kind:"method",key:"updated",value:function updated(){if("ontouchstart"in document.documentElement){// console.log("firstUpdated", this.shadowRoot!.getElementById("iosSlider"));
const slider=this.shadowRoot.getElementById("iosSlider");slider.style.userSelect="none";slider.style.touchAction="manipulation";// Listen for events
["touchstart","touchmove","touchend"].forEach(type=>{slider.addEventListener(type,event=>this.set(event),false);});}}},{kind:"method",key:"render",value:function render(){if(!this.hass||!this.stateObj){return $``;}return $`
      ${this.settingsOn===true?this._render_slider():this._render_colorPicker()}
    `;}},{kind:"method",key:"_render_slider",value:function _render_slider(){var _this$stateObj,_this$stateObj2,_this$stateObj3,_this$stateObj4,_this$stateObj5,_this$stateObj6,_this$stateObj7,_this$stateObj8,_this$stateObj9;if(!this.hass||!this.stateObj){return $``;}const supportDimming=lightSupportsDimming(this.stateObj);const brightness=(_this$stateObj=this.stateObj)!==null&&_this$stateObj!==void 0&&_this$stateObj.attributes.brightness?Math.round(this.stateObj.attributes.brightness/2.55):0;const switchValue=((_this$stateObj2=this.stateObj)===null||_this$stateObj2===void 0?void 0:_this$stateObj2.state)==="on"?1:0;const color=this._getColorForLightEntity(this.stateObj,undefined,undefined);let actions;const entity=(_this$stateObj3=this.stateObj)===null||_this$stateObj3===void 0?void 0:_this$stateObj3.entity_id;if(((_this$stateObj4=this.stateObj)===null||_this$stateObj4===void 0?void 0:_this$stateObj4.attributes.supported_color_modes[0])==="hs"||((_this$stateObj5=this.stateObj)===null||_this$stateObj5===void 0?void 0:_this$stateObj5.attributes.supported_color_modes[0])==="rgb"||((_this$stateObj6=this.stateObj)===null||_this$stateObj6===void 0?void 0:_this$stateObj6.attributes.supported_color_modes[0])==="rgbw"){actions=[{service_data:{entity_id:entity,rgb_color:[240,85,68]},color:"#f05544"},{service_data:{entity_id:entity,rgb_color:[125,219,84]},color:"#7DDB54"},{service_data:{entity_id:entity,rgb_color:[17,34,68]},color:"#112244"},{service_data:{entity_id:entity,rgb_color:[247,217,89]},color:"#f7d959"},{service_data:{entity_id:entity,rgb_color:[136,119,119]},color:"#887777"},{service_data:{entity_id:entity,rgb_color:[255,181,245]},color:"#FFB5F5"}];}else if(((_this$stateObj7=this.stateObj)===null||_this$stateObj7===void 0?void 0:_this$stateObj7.attributes.supported_color_modes[0])==="brightness"){actions=[{service_data:{entity_id:entity,brightness:65},color:"#D1CFCF"},{service_data:{entity_id:entity,brightness:120},color:"#DCDCDC"},{service_data:{entity_id:entity,brightness:220},color:"#F0F0F0"}];}let actionRowCount=0;if(actions){const numberOfRows=Math.ceil(actions.length/3);for(let i=0;i<numberOfRows;i++){this.actionRows[i]=[];for(let j=0;j<3;j++){if(actions[i*3+j]){this.actionRows[i][j]=actions[i*3+j];}}}}return $` <div class="content">
      ${supportDimming?$`
            <h2 id="brightnessValue">
              ${((_this$stateObj8=this.stateObj)===null||_this$stateObj8===void 0?void 0:_this$stateObj8.state)==="off"?this.hass.localize("component.light.state._.off"):brightness+"%"}
            </h2>
            <div class="range-holder">
              <input
                type="range"
                id="iosSlider"
                style=" --slider-width: 130px;
              --slider-height: 330px; --slider-border-radius: 40px;
              --slider-color:${color}; --slider-thumb-color:#ddd;
              --slider-track-color:#ddd"
                .value=${((_this$stateObj9=this.stateObj)===null||_this$stateObj9===void 0?void 0:_this$stateObj9.state)==="off"?String(0):String(brightness)}
                @change=${e=>this._setBrightness(this.stateObj,e.target.value)}
              />
            </div>
          `:$`
            <h2 id="switchValue">
              ${computeStateDisplay(this.hass.localize,this.stateObj,this.hass.locale)}
            </h2>

            <!-- <label id="SwitchContainer">
              <input
                id="iosSwitch"
                type="checkbox"
                ?checked=${!!switchValue}
                @change=${()=>this._switch(this.stateObj)}
              />
              <div id="SliderTrack"></div>
            </label> -->
            <div class="switch-holder">
              <input
                class="sliderOnOff ${o({switchON:switchValue===1,switchOFF:switchValue===0})}"
                type="range"
                id="iosSlider"
                style="--switch-width: 150px;
                --switch-height: 380px;
                --slider-border-radius: 40px;
                --switch-track-color: #ddd;"
                value="0"
                min="0"
                max="1"
                .value=${String(switchValue)}
                @change=${()=>this._switch(this.stateObj)}
              />
            </div>
          `}
      ${actions&&actions.length>0?$`
            <div class="action-holder">
              ${this.actionRows.map(actionRow=>{actionRowCount++;let actionCount=0;return $` <div class="action-row">
                  ${actionRow.map(action=>{actionCount++;return $` <div
                      class="action"
                      style="--size: 45px;"
                      @click=${e=>this._activateAction(e)}
                      data-service="${actionRowCount}#${actionCount}"
                    >
                      <span
                        class="color"
                        style="background-color:${action.color};
                                        border-color:${action.color};
                                        --size:50px"
                        ;
                      >
                      </span>
                    </div>`;})}
                </div>`;})}
            </div>
          `:$``}
      <div class="contentfooter">
        <ha-icon-button
          class="settings"
          .path=${"M8 13C6.14 13 4.59 14.28 4.14 16H2V18H4.14C4.59 19.72 6.14 21 8 21S11.41 19.72 11.86 18H22V16H11.86C11.41 14.28 9.86 13 8 13M8 19C6.9 19 6 18.1 6 17C6 15.9 6.9 15 8 15S10 15.9 10 17C10 18.1 9.1 19 8 19M19.86 6C19.41 4.28 17.86 3 16 3S12.59 4.28 12.14 6H2V8H12.14C12.59 9.72 14.14 11 16 11S19.41 9.72 19.86 8H22V6H19.86M16 9C14.9 9 14 8.1 14 7C14 5.9 14.9 5 16 5S18 5.9 18 7C18 8.1 17.1 9 16 9Z"}
          @click=${()=>this._openSettings()}
        ></ha-icon-button>
      </div>
    </div>`;}},{kind:"method",key:"_render_colorPicker",value:function _render_colorPicker(){var _attributes$effect_li;if(!this.hass||!this.stateObj){return $``;}const supportsTemp=lightSupportsColorMode(this.stateObj,LightColorModes.COLOR_TEMP);const supportsWhite=lightSupportsColorMode(this.stateObj,LightColorModes.WHITE);const supportsRgbww=lightSupportsColorMode(this.stateObj,LightColorModes.RGBWW);const supportsRgbw=!supportsRgbww&&lightSupportsColorMode(this.stateObj,LightColorModes.RGBW);const supportsColor=supportsRgbww||supportsRgbw||lightSupportsColor(this.stateObj);return $`
      <div class="content">
        ${lightSupportsDimming(this.stateObj)?$`
              <ha-labeled-slider
                caption=${this.hass.localize("ui.card.light.brightness")}
                icon="hass:brightness-5"
                min="0"
                max="100"
                value=${this._brightnessSliderValue}
                @change=${this._brightnessSliderChanged}
                pin
              ></ha-labeled-slider>
            `:""}
        ${this.stateObj.state==="on"?$`
              ${supportsTemp||supportsColor?$`<hr />`:""}
              ${supportsColor&&(supportsTemp||supportsWhite)?$`<ha-button-toggle-group
                    fullWidth
                    .buttons=${this._toggleButtons(supportsTemp,supportsWhite)}
                    .active=${this._mode}
                    @value-changed=${this._modeChanged}
                  ></ha-button-toggle-group>`:""}
              ${supportsTemp&&(!supportsColor&&!supportsWhite||this._mode===LightColorModes.COLOR_TEMP)?$`
                    <ha-labeled-slider
                      class="color_temp"
                      caption=${this.hass.localize("ui.card.light.color_temperature")}
                      icon="hass:thermometer"
                      .min=${this.stateObj.attributes.min_mireds}
                      .max=${this.stateObj.attributes.max_mireds}
                      .value=${this._ctSliderValue}
                      @change=${this._ctSliderChanged}
                      pin
                    ></ha-labeled-slider>
                  `:""}
              ${supportsColor&&(!supportsTemp&&!supportsWhite||this._mode==="color")?$`
                    <div class="segmentationContainer">
                      <ha-color-picker
                        class="color"
                        @colorselected=${this._colorPicked}
                        .desiredRgbColor=${this._colorPickerColor}
                        throttle="500"
                        .hueSegments=${this._hueSegments}
                        .saturationSegments=${this._saturationSegments}
                      >
                      </ha-color-picker>
                      <ha-icon-button
                        .path=${mdiPalette}
                        @click=${this._segmentClick}
                        class="segmentationButton"
                      ></ha-icon-button>
                    </div>

                    ${supportsRgbw||supportsRgbww?$`<ha-labeled-slider
                          .caption=${this.hass.localize("ui.card.light.color_brightness")}
                          icon="hass:brightness-7"
                          max="100"
                          .value=${this._colorBrightnessSliderValue}
                          @change=${this._colorBrightnessSliderChanged}
                          pin
                        ></ha-labeled-slider>`:""}
                    ${supportsRgbw?$`
                          <ha-labeled-slider
                            .caption=${this.hass.localize("ui.card.light.white_value")}
                            icon="hass:file-word-box"
                            max="100"
                            .name=${"wv"}
                            .value=${this._wvSliderValue}
                            @change=${this._wvSliderChanged}
                            pin
                          ></ha-labeled-slider>
                        `:""}
                    ${supportsRgbww?$`
                          <ha-labeled-slider
                            .caption=${this.hass.localize("ui.card.light.cold_white_value")}
                            icon="hass:file-word-box-outline"
                            max="100"
                            .name=${"cw"}
                            .value=${this._cwSliderValue}
                            @change=${this._wvSliderChanged}
                            pin
                          ></ha-labeled-slider>
                          <ha-labeled-slider
                            .caption=${this.hass.localize("ui.card.light.warm_white_value")}
                            icon="hass:file-word-box"
                            max="100"
                            .name=${"ww"}
                            .value=${this._wwSliderValue}
                            @change=${this._wvSliderChanged}
                            pin
                          ></ha-labeled-slider>
                        `:""}
                  `:""}
              ${supportsFeature(this.stateObj,SUPPORT_EFFECT)&&(_attributes$effect_li=this.stateObj.attributes.effect_list)!==null&&_attributes$effect_li!==void 0&&_attributes$effect_li.length?$`
                    <hr />
                    <ha-select
                      .label=${this.hass.localize("ui.card.light.effect")}
                      .value=${this.stateObj.attributes.effect||""}
                      fixedMenuPosition
                      naturalMenuWidth
                      @selected=${this._effectChanged}
                      @closed=${stopPropagation}
                    >
                      ${this.stateObj.attributes.effect_list.map(effect=>$`
                          <mwc-list-item .value=${effect}>
                            ${effect}
                          </mwc-list-item>
                        `)}
                    </ha-select>
                  `:""}
            `:""}
        <ha-attributes
          .hass=${this.hass}
          .stateObj=${this.stateObj}
          extra-filters="brightness,color_temp,white_value,effect_list,effect,hs_color,rgb_color,rgbw_color,rgbww_color,xy_color,min_mireds,max_mireds,entity_id,supported_color_modes,color_mode"
        ></ha-attributes>
        <div class="contentfooter">
          <mwc-button
            slot="primaryAction"
            @click=${()=>this._closeSettings()}
            class="settings"
          >
            ${this.hass.localize("ui.common.back")}
          </mwc-button>
        </div>
      </div>
      <!-- <ha-icon-button
        class="settings"
        .path=${"M8 13C6.14 13 4.59 14.28 4.14 16H2V18H4.14C4.59 19.72 6.14 21 8 21S11.41 19.72 11.86 18H22V16H11.86C11.41 14.28 9.86 13 8 13M8 19C6.9 19 6 18.1 6 17C6 15.9 6.9 15 8 15S10 15.9 10 17C10 18.1 9.1 19 8 19M19.86 6C19.41 4.28 17.86 3 16 3S12.59 4.28 12.14 6H2V8H12.14C12.59 9.72 14.14 11 16 11S19.41 9.72 19.86 8H22V6H19.86M16 9C14.9 9 14 8.1 14 7C14 5.9 14.9 5 16 5S18 5.9 18 7C18 8.1 17.1 9 16 9Z"}
        @click=${()=>this._closeSettings()}
      ></ha-icon-button> -->
    `;}},{kind:"method",key:"willUpdate",value:function willUpdate(changedProps){_get(_getPrototypeOf(MoreInfoLight.prototype),"willUpdate",this).call(this,changedProps);if(!changedProps.has("stateObj")){return;}const stateObj=this.stateObj;const oldStateObj=changedProps.get("stateObj");if(stateObj.state==="on"){// Don't change tab when the color mode changes
if((oldStateObj===null||oldStateObj===void 0?void 0:oldStateObj.entity_id)!==stateObj.entity_id||(oldStateObj===null||oldStateObj===void 0?void 0:oldStateObj.state)!==stateObj.state){this._mode=lightIsInColorMode(this.stateObj)?"color":this.stateObj.attributes.color_mode;}let brightnessAdjust=100;this._brightnessAdjusted=undefined;if(stateObj.attributes.color_mode===LightColorModes.RGB&&!lightSupportsColorMode(stateObj,LightColorModes.RGBWW)&&!lightSupportsColorMode(stateObj,LightColorModes.RGBW)){const maxVal=Math.max(...stateObj.attributes.rgb_color);if(maxVal<255){this._brightnessAdjusted=maxVal;brightnessAdjust=this._brightnessAdjusted/255*100;}}this._brightnessSliderValue=Math.round(stateObj.attributes.brightness*brightnessAdjust/255);this._ctSliderValue=stateObj.attributes.color_temp;this._wvSliderValue=stateObj.attributes.color_mode===LightColorModes.RGBW?Math.round(stateObj.attributes.rgbw_color[3]*100/255):undefined;this._cwSliderValue=stateObj.attributes.color_mode===LightColorModes.RGBWW?Math.round(stateObj.attributes.rgbww_color[3]*100/255):undefined;this._wwSliderValue=stateObj.attributes.color_mode===LightColorModes.RGBWW?Math.round(stateObj.attributes.rgbww_color[4]*100/255):undefined;const currentRgbColor=getLightCurrentModeRgbColor(stateObj);this._colorBrightnessSliderValue=currentRgbColor?Math.round(Math.max(...currentRgbColor.slice(0,3))*100/255):undefined;this._colorPickerColor=currentRgbColor===null||currentRgbColor===void 0?void 0:currentRgbColor.slice(0,3);}else {this._brightnessSliderValue=0;}}},{kind:"method",key:"_switch",value:function _switch(state){this.hass.callService("homeassistant","toggle",{entity_id:state.entity_id});}},{kind:"method",key:"_setBrightness",value:function _setBrightness(stateObj,value){this.hass.callService("homeassistant","turn_on",{entity_id:stateObj.entity_id,brightness:value*2.55});}},{kind:"method",key:"_activateAction",value:function _activateAction(e){if(e.target.dataset&&e.target.dataset.service){const[row,item]=e.target.dataset.service.split("#",2);const action=this.actionRows[row-1][item-1];this.hass.callService("light","turn_on",action.service_data);}}},{kind:"method",key:"_getColorForLightEntity",value:function _getColorForLightEntity(stateObj,useTemperature,useBrightness){let color;if(stateObj){if(stateObj.attributes.rgb_color){color=`rgb(${stateObj.attributes.rgb_color.join(",")})`;if(stateObj.attributes.brightness){color=this._applyBrightnessToColor(color,(stateObj.attributes.brightness+245)/5);}}else if(useTemperature&&stateObj.attributes.color_temp&&stateObj.attributes.min_mireds&&stateObj.attributes.max_mireds){color=this._getLightColorBasedOnTemperature(stateObj.attributes.color_temp,stateObj.attributes.min_mireds,stateObj.attributes.max_mireds);if(stateObj.attributes.brightness){color=this._applyBrightnessToColor(color,(stateObj.attributes.brightness+245)/5);}}else if(useBrightness&&stateObj.attributes.brightness){color=this._applyBrightnessToColor(this._getDefaultColorForState(),(stateObj.attributes.brightness+245)/5);}else {color=this._getDefaultColorForState();}}return color;}},{kind:"method",key:"_applyBrightnessToColor",value:function _applyBrightnessToColor(color,brightness){const colorObj=new TinyColor(this._getColorFromVariable(color));if(colorObj.isValid){const validColor=colorObj.mix("black",100-brightness).toString();if(validColor)return validColor;}return color;}},{kind:"method",key:"_getColorFromVariable",value:function _getColorFromVariable(color){if(typeof color!=="undefined"&&color.substring(0,3)==="var"){return window.getComputedStyle(document.documentElement).getPropertyValue(color.substring(4).slice(0,-1)).trim();}return color;}},{kind:"method",key:"_getLightColorBasedOnTemperature",value:function _getLightColorBasedOnTemperature(current,min,max){const high=new TinyColor("rgb(255, 160, 0)");//  orange-ish
const low=new TinyColor("rgb(166, 209, 255)");//  blue-ish
const middle=new TinyColor("white");const mixAmount=(current-min)/(max-min)*100;if(mixAmount<50){return tinycolor(low).mix(middle,mixAmount*2).toRgbString();}return tinycolor(middle).mix(high,(mixAmount-50)*2).toRgbString();}},{kind:"method",key:"_getDefaultColorForState",value:function _getDefaultColorForState(){return "#f7d959";}},{kind:"method",key:"_openSettings",value:function _openSettings(){this.settingsOn=false;}},{kind:"method",key:"_closeSettings",value:function _closeSettings(){this.settingsOn=true;}},{kind:"field",key:"_toggleButtons",value(){return memoizeOne((supportsTemp,supportsWhite)=>{const modes=[{label:"Color",value:"color"}];if(supportsTemp){modes.push({label:"Temperature",value:LightColorModes.COLOR_TEMP});}if(supportsWhite){modes.push({label:"White",value:LightColorModes.WHITE});}return modes;});}},{kind:"method",key:"_modeChanged",value:function _modeChanged(ev){this._mode=ev.detail.value;}},{kind:"method",key:"_effectChanged",value:function _effectChanged(ev){const newVal=ev.target.value;if(!newVal||this.stateObj.attributes.effect===newVal){return;}this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,effect:newVal});}},{kind:"method",key:"_brightnessSliderChanged",value:function _brightnessSliderChanged(ev){const bri=Number(ev.target.value);if(isNaN(bri)){return;}this._brightnessSliderValue=bri;if(this._mode===LightColorModes.WHITE){this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,white:Math.min(255,Math.round(bri*255/100))});return;}if(this._brightnessAdjusted){const rgb=this.stateObj.attributes.rgb_color||[0,0,0];this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,brightness_pct:bri,rgb_color:this._adjustColorBrightness(rgb,this._brightnessAdjusted,true)});return;}this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,brightness_pct:bri});}},{kind:"method",key:"_ctSliderChanged",value:function _ctSliderChanged(ev){const ct=Number(ev.target.value);if(isNaN(ct)){return;}this._ctSliderValue=ct;this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,color_temp:ct});}},{kind:"method",key:"_wvSliderChanged",value:function _wvSliderChanged(ev){const target=ev.target;let wv=Number(target.value);const name=target.name;if(isNaN(wv)){return;}if(name==="wv"){this._wvSliderValue=wv;}else if(name==="cw"){this._cwSliderValue=wv;}else if(name==="ww"){this._wwSliderValue=wv;}wv=Math.min(255,Math.round(wv*255/100));const rgb=getLightCurrentModeRgbColor(this.stateObj);if(name==="wv"){const rgbw_color=rgb||[0,0,0,0];rgbw_color[3]=wv;this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,rgbw_color});return;}const rgbww_color=rgb||[0,0,0,0,0];while(rgbww_color.length<5){rgbww_color.push(0);}rgbww_color[name==="cw"?3:4]=wv;this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,rgbww_color});}},{kind:"method",key:"_colorBrightnessSliderChanged",value:function _colorBrightnessSliderChanged(ev){var _getLightCurrentModeR;const target=ev.target;let value=Number(target.value);if(isNaN(value)){return;}const oldValue=this._colorBrightnessSliderValue;this._colorBrightnessSliderValue=value;value=value*255/100;const rgb=((_getLightCurrentModeR=getLightCurrentModeRgbColor(this.stateObj))===null||_getLightCurrentModeR===void 0?void 0:_getLightCurrentModeR.slice(0,3))||[255,255,255];this._setRgbWColor(this._adjustColorBrightness(// first normalize the value
oldValue?this._adjustColorBrightness(rgb,oldValue*255/100,true):rgb,value));}},{kind:"method",key:"_segmentClick",value:function _segmentClick(){if(this._hueSegments===24&&this._saturationSegments===8){this._hueSegments=0;this._saturationSegments=0;}else {this._hueSegments=24;this._saturationSegments=8;}}},{kind:"method",key:"_adjustColorBrightness",value:function _adjustColorBrightness(rgbColor,value,invert=false){if(value!==undefined&&value!==255){let ratio=value/255;if(invert){ratio=1/ratio;}rgbColor[0]=Math.min(255,Math.round(rgbColor[0]*ratio));rgbColor[1]=Math.min(255,Math.round(rgbColor[1]*ratio));rgbColor[2]=Math.min(255,Math.round(rgbColor[2]*ratio));}return rgbColor;}},{kind:"method",key:"_setRgbWColor",value:function _setRgbWColor(rgbColor){if(lightSupportsColorMode(this.stateObj,LightColorModes.RGBWW)){const rgbww_color=this.stateObj.attributes.rgbww_color?[...this.stateObj.attributes.rgbww_color]:[0,0,0,0,0];this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,rgbww_color:rgbColor.concat(rgbww_color.slice(3))});}else if(lightSupportsColorMode(this.stateObj,LightColorModes.RGBW)){const rgbw_color=this.stateObj.attributes.rgbw_color?[...this.stateObj.attributes.rgbw_color]:[0,0,0,0];this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,rgbw_color:rgbColor.concat(rgbw_color.slice(3))});}}/**
   * Called when a new color has been picked.
   * should be throttled with the 'throttle=' attribute of the color picker
   */},{kind:"method",key:"_colorPicked",value:function _colorPicked(ev){this._colorPickerColor=[ev.detail.rgb.r,ev.detail.rgb.g,ev.detail.rgb.b];if(lightSupportsColorMode(this.stateObj,LightColorModes.RGBWW)||lightSupportsColorMode(this.stateObj,LightColorModes.RGBW)){this._setRgbWColor(this._colorBrightnessSliderValue?this._adjustColorBrightness([ev.detail.rgb.r,ev.detail.rgb.g,ev.detail.rgb.b],this._colorBrightnessSliderValue*255/100):[ev.detail.rgb.r,ev.detail.rgb.g,ev.detail.rgb.b]);}else if(lightSupportsColorMode(this.stateObj,LightColorModes.RGB)){const rgb_color=[ev.detail.rgb.r,ev.detail.rgb.g,ev.detail.rgb.b];if(this._brightnessAdjusted){this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,brightness_pct:this._brightnessSliderValue,rgb_color:this._adjustColorBrightness(rgb_color,this._brightnessAdjusted,true)});}else {this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,rgb_color});}}else {this.hass.callService("light","turn_on",{entity_id:this.stateObj.entity_id,hs_color:[ev.detail.hs.h,ev.detail.hs.s*100]});}}},{kind:"get",static:true,key:"styles",value:function styles(){return r`
      :host {
        background-color: #000 !important;
      }
      .popup-wrapper {
        margin-top: 64px;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
      }

      .range-holder {
        --slider-height: 380px;
        --slider-width: 150px;
        height: var(--slider-height);
        width: var(--slider-width);
        position: relative;
        display: block;
      }
      .range-holder input[type="range"] {
        outline: 0;
        border: 0;
        border-radius: var(--slider-border-radius, 12px);
        width: var(--slider-height);
        margin: 0;
        transition: box-shadow 0.2s ease-in-out;
        -webkit-transform: rotate(270deg);
        -moz-transform: rotate(270deg);
        -o-transform: rotate(270deg);
        -ms-transform: rotate(270deg);
        transform: rotate(270deg);
        overflow: hidden;
        height: var(--slider-width);
        -webkit-appearance: none;
        background-color: var(--slider-track-color);
        position: absolute;
        top: calc(50% - (var(--slider-width) / 2));
        right: calc(50% - (var(--slider-height) / 2));
      }
      .range-holder input[type="range"]::-webkit-slider-runnable-track {
        height: var(--slider-width);
        -webkit-appearance: none;
        background-color: var(--slider-track-color);
        margin-top: -1px;
        transition: box-shadow 0.2s ease-in-out;
      }
      .range-holder input[type="range"]::-webkit-slider-thumb {
        width: 25px;
        border-right: 10px solid var(--slider-color);
        border-left: 10px solid var(--slider-color);
        border-top: 20px solid var(--slider-color);
        border-bottom: 20px solid var(--slider-color);
        -webkit-appearance: none;
        height: 80px;
        cursor: grabbing;
        background: var(--slider-color);
        box-shadow: -350px 0 0 350px var(--slider-color),
          inset 0 0 0 80px var(--slider-thumb-color);
        border-radius: 0;
        transition: box-shadow 0.2s ease-in-out;
        position: relative;
        top: calc((var(--slider-width) - 80px) / 2);
      }
      .range-holder input[type="range"]::-moz-thumb-track {
        height: var(--slider-width);
        background-color: var(--slider-track-color);
        margin-top: -1px;
        transition: box-shadow 0.2s ease-in-out;
      }
      .range-holder input[type="range"]::-moz-range-thumb {
        width: 5px;
        border-right: 12px solid var(--slider-color);
        border-left: 12px solid var(--slider-color);
        border-top: 20px solid var(--slider-color);
        border-bottom: 20px solid var(--slider-color);
        height: calc(var(--slider-width) * 0.4);
        cursor: ew-resize;
        background: var(--slider-color);
        box-shadow: -350px 0 0 350px var(--slider-color),
          inset 0 0 0 80px var(--slider-thumb-color);
        border-radius: 0;
        transition: box-shadow 0.2s ease-in-out;
        position: relative;
        top: calc((var(--slider-width) - 80px) / 2);
      }
      #brightnessValue {
        text-align: center;
        margin: 0;
      }
      .switch-holder {
        --switch-height: 380px;
        --switch-width: 150px;
        height: var(--switch-height);
        width: var(--switch-width);
        position: relative;
        display: block;
      }
      #switchValue {
        text-align: center;
      }
      .switch-holder input[type="range"] {
        outline: 0;
        border: 0;
        border-radius: var(--slider-border-radius, 12px);
        width: calc(var(--switch-height) - 20px);
        margin: 0;
        transition: 1s ease-in-out;
        -webkit-transform: rotate(270deg);
        -moz-transform: rotate(270deg);
        -o-transform: rotate(270deg);
        -ms-transform: rotate(270deg);
        transform: rotate(270deg);
        overflow: hidden;
        height: calc(var(--switch-width) - 20px);
        -webkit-appearance: none;
        background-color: var(--switch-track-color);
        padding: 10px;
        position: absolute;
        top: calc(50% - (var(--switch-width) / 2));
        right: calc(50% - (var(--switch-height) / 2));
      }
      .switch-holder input[type="range"]::-webkit-slider-runnable-track {
        height: calc(var(--switch-width) - 20px);
        -webkit-appearance: none;
        color: var(--switch-track-color);
        margin-top: -1px;
        transition: 0.2s ease-in-out;
      }
      .switch-holder input[type="range"]::-webkit-slider-thumb {
        width: calc(var(--switch-height) / 2);
        -webkit-appearance: none;
        height: calc(var(--switch-width) - 20px);
        cursor: ew-resize;
        background: var(--switch-color);
        transition: 0.2s ease-in-out;
        border: none;
        /* box-shadow: -1px 1px 20px 0px rgba(0, 0, 0, 0.75); */
        position: relative;
        top: 0;
        border-radius: var(--slider-border-radius, 12px);
      }

      .action-holder {
        display: flex;
        flex-direction: column;
        /* margin-top: 20px; */
      }
      .action-row {
        display: block;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 10px;
      }
      .action-row:last-child {
        padding: 0;
      }
      .action-holder .action {
        display: inline-block;
        margin-right: 4px;
        margin-left: 4px;
        cursor: pointer;
      }
      .action-holder.action:nth-child(4n) {
        margin-right: 0;
      }
      .action-holder .action .color {
        width: var(--size);
        height: var(--size);
        border-radius: 50%;
        display: block;
        border: 1px solid #fff;
        line-height: var(--size);
        text-align: center;
        pointer-events: none;
      }
      .action-holder .action .color ha-icon {
        pointer-events: none;
      }
      .action-holder .action .name {
        width: var(--size);
        display: block;
        color: #fff;
        font-size: 9px;
        margin-top: 3px;
        text-align: center;
        pointer-events: none;
      }
      .sliderOnOff input[type="range"] {
        transition: 1s ease-in-out;
      }
      .switchON {
        --switch-color: var(--switch-checked-button-color);
      }
      .switchOFF {
        --switch-color: var(--switch-unchecked-button-color);
      }
      .content {
        display: flex;
        flex-direction: column;
        align-items: center;
      }

      .content > * {
        width: 100%;
      }
      .contentfooter {
        position: relative;
        width: 100%;
        height: 45px;
      }

      .settings {
        position: absolute;
        bottom: 0;
        right: 0;
        width: auto;
        height: auto;
      }
      .color_temp {
        --ha-slider-background: -webkit-linear-gradient(
          right,
          rgb(255, 160, 0) 0%,
          white 50%,
          rgb(166, 209, 255) 100%
        );
        /* The color temp minimum value shouldn't be rendered differently. It's not "off". */
        --paper-slider-knob-start-border-color: var(--primary-color);
        margin-bottom: 4px;
      }

      .segmentationContainer {
        position: relative;
        max-height: 500px;
        display: flex;
        justify-content: center;
      }

      ha-button-toggle-group {
        margin-bottom: 8px;
      }

      ha-color-picker {
        --ha-color-picker-wheel-borderwidth: 5;
        --ha-color-picker-wheel-bordercolor: white;
        --ha-color-picker-wheel-shadow: none;
        --ha-color-picker-marker-borderwidth: 2;
        --ha-color-picker-marker-bordercolor: white;
      }

      .segmentationButton {
        position: absolute;
        top: 5%;
        left: 0;
        color: var(--secondary-text-color);
      }

      hr {
        border-color: var(--divider-color);
        border-bottom: none;
        margin: 16px 0;
      }

      #SwitchContainer {
        background: #f0f0f0;
        height: 260px;
        width: 90px;
        border-radius: 20px;
        cursor: pointer;
        position: relative;
        margin-top: 15%;
        margin-bottom: 20%;
      }

      #iosSwitch {
        opacity: 0;
        width: 0;
        height: 0;
      }

      #SwitchContainer:before {
        -webkit-transform: translateY(-125px);
        -ms-transform: translateY(-125px);
        transform: translateY(-125px);
      }

      #iosSwitch:checked {
        -webkit-transform: translateY(-125px);
        -ms-transform: translateY(-125px);
        transform: translateY(-125px);
      }

      #SliderTrack {
        -webkit-transition: 0.4s;
        transition: 0.4s;
      }

      #SliderTrack::before {
        position: absolute;
        content: "";
        margin: 5px 0 0 5px;
        height: 125px;
        width: 80px;
        left: 0px;
        top: 125px;
        -webkit-transition: 0.4s;
        transition: 0.4s;
        border-radius: 18px;
        background-color: #f8cc46;
      }
    `;}}]};},s);
