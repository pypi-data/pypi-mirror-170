const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { aI as intlLocalematcher_1, aJ as intlLocalematcher_2, O as createCommonjsModule, P as unwrapExports, aK as intlLocalematcher } from './auth-dev.js';
import { U as __extends, et as tslib_es6 } from './main-dev.js';
import './stop_propagation-dev.js';

/**
 * http://ecma-international.org/ecma-402/7.0/index.html#sec-canonicalizelocalelist
 * @param locales
 */function CanonicalizeLocaleList(locales){// TODO
return Intl.getCanonicalLocales(locales);}

/**
 * https://tc39.es/ecma402/#sec-canonicalizetimezonename
 * @param tz
 */function CanonicalizeTimeZoneName(tz,_a){var tzData=_a.tzData,uppercaseLinks=_a.uppercaseLinks;var uppercasedTz=tz.toUpperCase();var uppercasedZones=Object.keys(tzData).reduce(function(all,z){all[z.toUpperCase()]=z;return all;},{});var ianaTimeZone=uppercaseLinks[uppercasedTz]||uppercasedZones[uppercasedTz];if(ianaTimeZone==='Etc/UTC'||ianaTimeZone==='Etc/GMT'){return 'UTC';}return ianaTimeZone;}

/**
 * https://tc39.es/ecma262/#sec-tostring
 */function ToString(o){// Only symbol is irregular...
if(typeof o==='symbol'){throw TypeError('Cannot convert a Symbol value to a string');}return String(o);}/**
 * https://tc39.es/ecma262/#sec-tonumber
 * @param val
 */function ToNumber(val){if(val===undefined){return NaN;}if(val===null){return +0;}if(typeof val==='boolean'){return val?1:+0;}if(typeof val==='number'){return val;}if(typeof val==='symbol'||typeof val==='bigint'){throw new TypeError('Cannot convert symbol/bigint to number');}return Number(val);}/**
 * https://tc39.es/ecma262/#sec-tointeger
 * @param n
 */function ToInteger(n){var number=ToNumber(n);if(isNaN(number)||SameValue(number,-0)){return 0;}if(isFinite(number)){return number;}var integer=Math.floor(Math.abs(number));if(number<0){integer=-integer;}if(SameValue(integer,-0)){return 0;}return integer;}/**
 * https://tc39.es/ecma262/#sec-timeclip
 * @param time
 */function TimeClip(time){if(!isFinite(time)){return NaN;}if(Math.abs(time)>8.64*1e15){return NaN;}return ToInteger(time);}/**
 * https://tc39.es/ecma262/#sec-toobject
 * @param arg
 */function ToObject(arg){if(arg==null){throw new TypeError('undefined/null cannot be converted to object');}return Object(arg);}/**
 * https://www.ecma-international.org/ecma-262/11.0/index.html#sec-samevalue
 * @param x
 * @param y
 */function SameValue(x,y){if(Object.is){return Object.is(x,y);}// SameValue algorithm
if(x===y){// Steps 1-5, 7-10
// Steps 6.b-6.e: +0 != -0
return x!==0||1/x===1/y;}// Step 6.a: NaN == NaN
return x!==x&&y!==y;}/**
 * https://www.ecma-international.org/ecma-262/11.0/index.html#sec-arraycreate
 * @param len
 */function ArrayCreate(len){return new Array(len);}/**
 * https://www.ecma-international.org/ecma-262/11.0/index.html#sec-hasownproperty
 * @param o
 * @param prop
 */function HasOwnProperty(o,prop){return Object.prototype.hasOwnProperty.call(o,prop);}/**
 * https://www.ecma-international.org/ecma-262/11.0/index.html#sec-type
 * @param x
 */function Type(x){if(x===null){return 'Null';}if(typeof x==='undefined'){return 'Undefined';}if(typeof x==='function'||typeof x==='object'){return 'Object';}if(typeof x==='number'){return 'Number';}if(typeof x==='boolean'){return 'Boolean';}if(typeof x==='string'){return 'String';}if(typeof x==='symbol'){return 'Symbol';}if(typeof x==='bigint'){return 'BigInt';}}var MS_PER_DAY=86400000;/**
 * https://www.ecma-international.org/ecma-262/11.0/index.html#eqn-modulo
 * @param x
 * @param y
 * @return k of the same sign as y
 */function mod(x,y){return x-Math.floor(x/y)*y;}/**
 * https://tc39.es/ecma262/#eqn-Day
 * @param t
 */function Day(t){return Math.floor(t/MS_PER_DAY);}/**
 * https://tc39.es/ecma262/#sec-week-day
 * @param t
 */function WeekDay(t){return mod(Day(t)+4,7);}/**
 * https://tc39.es/ecma262/#sec-year-number
 * @param y
 */function DayFromYear(y){return Date.UTC(y,0)/MS_PER_DAY;}/**
 * https://tc39.es/ecma262/#sec-year-number
 * @param y
 */function TimeFromYear(y){return Date.UTC(y,0);}/**
 * https://tc39.es/ecma262/#sec-year-number
 * @param t
 */function YearFromTime(t){return new Date(t).getUTCFullYear();}function DaysInYear(y){if(y%4!==0){return 365;}if(y%100!==0){return 366;}if(y%400!==0){return 365;}return 366;}function DayWithinYear(t){return Day(t)-DayFromYear(YearFromTime(t));}function InLeapYear(t){return DaysInYear(YearFromTime(t))===365?0:1;}/**
 * https://tc39.es/ecma262/#sec-month-number
 * @param t
 */function MonthFromTime(t){var dwy=DayWithinYear(t);var leap=InLeapYear(t);if(dwy>=0&&dwy<31){return 0;}if(dwy<59+leap){return 1;}if(dwy<90+leap){return 2;}if(dwy<120+leap){return 3;}if(dwy<151+leap){return 4;}if(dwy<181+leap){return 5;}if(dwy<212+leap){return 6;}if(dwy<243+leap){return 7;}if(dwy<273+leap){return 8;}if(dwy<304+leap){return 9;}if(dwy<334+leap){return 10;}if(dwy<365+leap){return 11;}throw new Error('Invalid time');}function DateFromTime(t){var dwy=DayWithinYear(t);var mft=MonthFromTime(t);var leap=InLeapYear(t);if(mft===0){return dwy+1;}if(mft===1){return dwy-30;}if(mft===2){return dwy-58-leap;}if(mft===3){return dwy-89-leap;}if(mft===4){return dwy-119-leap;}if(mft===5){return dwy-150-leap;}if(mft===6){return dwy-180-leap;}if(mft===7){return dwy-211-leap;}if(mft===8){return dwy-242-leap;}if(mft===9){return dwy-272-leap;}if(mft===10){return dwy-303-leap;}if(mft===11){return dwy-333-leap;}throw new Error('Invalid time');}var HOURS_PER_DAY=24;var MINUTES_PER_HOUR=60;var SECONDS_PER_MINUTE=60;var MS_PER_SECOND=1e3;var MS_PER_MINUTE=MS_PER_SECOND*SECONDS_PER_MINUTE;var MS_PER_HOUR=MS_PER_MINUTE*MINUTES_PER_HOUR;function HourFromTime(t){return mod(Math.floor(t/MS_PER_HOUR),HOURS_PER_DAY);}function MinFromTime(t){return mod(Math.floor(t/MS_PER_MINUTE),MINUTES_PER_HOUR);}function SecFromTime(t){return mod(Math.floor(t/MS_PER_SECOND),SECONDS_PER_MINUTE);}function IsCallable(fn){return typeof fn==='function';}/**
 * The abstract operation OrdinaryHasInstance implements
 * the default algorithm for determining if an object O
 * inherits from the instance object inheritance path
 * provided by constructor C.
 * @param C class
 * @param O object
 * @param internalSlots internalSlots
 */function OrdinaryHasInstance(C,O,internalSlots){if(!IsCallable(C)){return false;}if(internalSlots===null||internalSlots===void 0?void 0:internalSlots.boundTargetFunction){var BC=internalSlots===null||internalSlots===void 0?void 0:internalSlots.boundTargetFunction;return O instanceof BC;}if(typeof O!=='object'){return false;}var P=C.prototype;if(typeof P!=='object'){throw new TypeError('OrdinaryHasInstance called on an object with an invalid prototype property.');}return Object.prototype.isPrototypeOf.call(P,O);}function msFromTime(t){return mod(t,MS_PER_SECOND);}

/**
 * https://tc39.es/ecma402/#sec-coerceoptionstoobject
 * @param options
 * @returns
 */function CoerceOptionsToObject(options){if(typeof options==='undefined'){return Object.create(null);}return ToObject(options);}

function DefaultNumberOption(val,min,max,fallback){if(val!==undefined){val=Number(val);if(isNaN(val)||val<min||val>max){throw new RangeError("".concat(val," is outside of range [").concat(min,", ").concat(max,"]"));}return Math.floor(val);}return fallback;}

function GetNumberOption(options,property,minimum,maximum,fallback){var val=options[property];// @ts-expect-error
return DefaultNumberOption(val,minimum,maximum,fallback);}

/**
 * https://tc39.es/ecma402/#sec-getoption
 * @param opts
 * @param prop
 * @param type
 * @param values
 * @param fallback
 */function GetOption(opts,prop,type,values,fallback){if(typeof opts!=='object'){throw new TypeError('Options must be an object');}var value=opts[prop];if(value!==undefined){if(type!=='boolean'&&type!=='string'){throw new TypeError('invalid type');}if(type==='boolean'){value=Boolean(value);}if(type==='string'){value=ToString(value);}if(values!==undefined&&!values.filter(function(val){return val==value;}).length){throw new RangeError("".concat(value," is not within ").concat(values.join(', ')));}return value;}return fallback;}

/**
 * https://tc39.es/ecma402/#sec-getoptionsobject
 * @param options
 * @returns
 */function GetOptionsObject(options){if(typeof options==='undefined'){return Object.create(null);}if(typeof options==='object'){return options;}throw new TypeError('Options must be an object');}

/**
 * https://tc39.es/ecma402/#table-sanctioned-simple-unit-identifiers
 */var SANCTIONED_UNITS=['angle-degree','area-acre','area-hectare','concentr-percent','digital-bit','digital-byte','digital-gigabit','digital-gigabyte','digital-kilobit','digital-kilobyte','digital-megabit','digital-megabyte','digital-petabyte','digital-terabit','digital-terabyte','duration-day','duration-hour','duration-millisecond','duration-minute','duration-month','duration-second','duration-week','duration-year','length-centimeter','length-foot','length-inch','length-kilometer','length-meter','length-mile-scandinavian','length-mile','length-millimeter','length-yard','mass-gram','mass-kilogram','mass-ounce','mass-pound','mass-stone','temperature-celsius','temperature-fahrenheit','volume-fluid-ounce','volume-gallon','volume-liter','volume-milliliter'];// In CLDR, the unit name always follows the form `namespace-unit` pattern.
// For example: `digital-bit` instead of `bit`. This function removes the namespace prefix.
function removeUnitNamespace(unit){return unit.slice(unit.indexOf('-')+1);}/**
 * https://tc39.es/ecma402/#table-sanctioned-simple-unit-identifiers
 */var SIMPLE_UNITS=SANCTIONED_UNITS.map(removeUnitNamespace);/**
 * https://tc39.es/ecma402/#sec-issanctionedsimpleunitidentifier
 */function IsSanctionedSimpleUnitIdentifier(unitIdentifier){return SIMPLE_UNITS.indexOf(unitIdentifier)>-1;}

/**
 * https://tc39.es/ecma402/#sec-isvalidtimezonename
 * @param tz
 * @param implDetails implementation details
 */function IsValidTimeZoneName(tz,_a){var tzData=_a.tzData,uppercaseLinks=_a.uppercaseLinks;var uppercasedTz=tz.toUpperCase();var zoneNames=new Set();var linkNames=new Set();Object.keys(tzData).map(function(z){return z.toUpperCase();}).forEach(function(z){return zoneNames.add(z);});Object.keys(uppercaseLinks).forEach(function(linkName){linkNames.add(linkName.toUpperCase());zoneNames.add(uppercaseLinks[linkName].toUpperCase());});return zoneNames.has(uppercasedTz)||linkNames.has(uppercasedTz);}

/**
 * This follows https://tc39.es/ecma402/#sec-case-sensitivity-and-case-mapping
 * @param str string to convert
 */function toUpperCase(str){return str.replace(/([a-z])/g,function(_,c){return c.toUpperCase();});}var NOT_A_Z_REGEX=/[^A-Z]/;/**
 * https://tc39.es/ecma402/#sec-iswellformedcurrencycode
 */function IsWellFormedCurrencyCode(currency){currency=toUpperCase(currency);if(currency.length!==3){return false;}if(NOT_A_Z_REGEX.test(currency)){return false;}return true;}

/**
 * This follows https://tc39.es/ecma402/#sec-case-sensitivity-and-case-mapping
 * @param str string to convert
 */function toLowerCase(str){return str.replace(/([A-Z])/g,function(_,c){return c.toLowerCase();});}/**
 * https://tc39.es/ecma402/#sec-iswellformedunitidentifier
 * @param unit
 */function IsWellFormedUnitIdentifier(unit){unit=toLowerCase(unit);if(IsSanctionedSimpleUnitIdentifier(unit)){return true;}var units=unit.split('-per-');if(units.length!==2){return false;}var numerator=units[0],denominator=units[1];if(!IsSanctionedSimpleUnitIdentifier(numerator)||!IsSanctionedSimpleUnitIdentifier(denominator)){return false;}return true;}

/**
 * Cannot do Math.log(x) / Math.log(10) bc if IEEE floating point issue
 * @param x number
 */function getMagnitude(x){// Cannot count string length via Number.toString because it may use scientific notation
// for very small or very large numbers.
return Math.floor(Math.log(x)*Math.LOG10E);}function repeat(s,times){if(typeof s.repeat==='function'){return s.repeat(times);}var arr=new Array(times);for(var i=0;i<arr.length;i++){arr[i]=s;}return arr.join('');}function setInternalSlot(map,pl,field,value){if(!map.get(pl)){map.set(pl,Object.create(null));}var slots=map.get(pl);slots[field]=value;}function setMultiInternalSlots(map,pl,props){for(var _i=0,_a=Object.keys(props);_i<_a.length;_i++){var k=_a[_i];setInternalSlot(map,pl,k,props[k]);}}function getInternalSlot(map,pl,field){return getMultiInternalSlots(map,pl,field)[field];}function getMultiInternalSlots(map,pl){var fields=[];for(var _i=2;_i<arguments.length;_i++){fields[_i-2]=arguments[_i];}var slots=map.get(pl);if(!slots){throw new TypeError("".concat(pl," InternalSlot has not been initialized"));}return fields.reduce(function(all,f){all[f]=slots[f];return all;},Object.create(null));}function isLiteralPart(patternPart){return patternPart.type==='literal';}/*
  17 ECMAScript Standard Built-in Objects:
    Every built-in Function object, including constructors, that is not
    identified as an anonymous function has a name property whose value
    is a String.

    Unless otherwise specified, the name property of a built-in Function
    object, if it exists, has the attributes { [[Writable]]: false,
    [[Enumerable]]: false, [[Configurable]]: true }.
*/function defineProperty(target,name,_a){var value=_a.value;Object.defineProperty(target,name,{configurable:true,enumerable:false,writable:true,value:value});}function invariant(condition,message,Err){if(Err===void 0){Err=Error;}if(!condition){throw new Err(message);}}

/**
 * The abstract operation ComputeExponentForMagnitude computes an exponent by which to scale a
 * number of the given magnitude (power of ten of the most significant digit) according to the
 * locale and the desired notation (scientific, engineering, or compact).
 */function ComputeExponentForMagnitude(numberFormat,magnitude,_a){var getInternalSlots=_a.getInternalSlots;var internalSlots=getInternalSlots(numberFormat);var notation=internalSlots.notation,dataLocaleData=internalSlots.dataLocaleData,numberingSystem=internalSlots.numberingSystem;switch(notation){case'standard':return 0;case'scientific':return magnitude;case'engineering':return Math.floor(magnitude/3)*3;default:{// Let exponent be an implementation- and locale-dependent (ILD) integer by which to scale a
// number of the given magnitude in compact notation for the current locale.
var compactDisplay=internalSlots.compactDisplay,style=internalSlots.style,currencyDisplay=internalSlots.currencyDisplay;var thresholdMap=void 0;if(style==='currency'&&currencyDisplay!=='name'){var currency=dataLocaleData.numbers.currency[numberingSystem]||dataLocaleData.numbers.currency[dataLocaleData.numbers.nu[0]];thresholdMap=currency.short;}else {var decimal=dataLocaleData.numbers.decimal[numberingSystem]||dataLocaleData.numbers.decimal[dataLocaleData.numbers.nu[0]];thresholdMap=compactDisplay==='long'?decimal.long:decimal.short;}if(!thresholdMap){return 0;}var num=String(Math.pow(10,magnitude));var thresholds=Object.keys(thresholdMap);// TODO: this can be pre-processed
if(num<thresholds[0]){return 0;}if(num>thresholds[thresholds.length-1]){return thresholds[thresholds.length-1].length-1;}var i=thresholds.indexOf(num);if(i===-1){return 0;}// See https://unicode.org/reports/tr35/tr35-numbers.html#Compact_Number_Formats
// Special handling if the pattern is precisely `0`.
var magnitudeKey=thresholds[i];// TODO: do we need to handle plural here?
var compactPattern=thresholdMap[magnitudeKey].other;if(compactPattern==='0'){return 0;}// Example: in zh-TW, `10000000` maps to `0000萬`. So we need to return 8 - 4 = 4 here.
return magnitudeKey.length-thresholdMap[magnitudeKey].other.match(/0+/)[0].length;}}}

function ToRawPrecision(x,minPrecision,maxPrecision){var p=maxPrecision;var m;var e;var xFinal;if(x===0){m=repeat('0',p);e=0;xFinal=0;}else {var xToString=x.toString();// If xToString is formatted as scientific notation, the number is either very small or very
// large. If the precision of the formatted string is lower that requested max precision, we
// should still infer them from the formatted string, otherwise the formatted result might have
// precision loss (e.g. 1e41 will not have 0 in every trailing digits).
var xToStringExponentIndex=xToString.indexOf('e');var _a=xToString.split('e'),xToStringMantissa=_a[0],xToStringExponent=_a[1];var xToStringMantissaWithoutDecimalPoint=xToStringMantissa.replace('.','');if(xToStringExponentIndex>=0&&xToStringMantissaWithoutDecimalPoint.length<=p){e=+xToStringExponent;m=xToStringMantissaWithoutDecimalPoint+repeat('0',p-xToStringMantissaWithoutDecimalPoint.length);xFinal=x;}else {e=getMagnitude(x);var decimalPlaceOffset=e-p+1;// n is the integer containing the required precision digits. To derive the formatted string,
// we will adjust its decimal place in the logic below.
var n=Math.round(adjustDecimalPlace(x,decimalPlaceOffset));// The rounding caused the change of magnitude, so we should increment `e` by 1.
if(adjustDecimalPlace(n,p-1)>=10){e=e+1;// Divide n by 10 to swallow one precision.
n=Math.floor(n/10);}m=n.toString();// Equivalent of n * 10 ** (e - p + 1)
xFinal=adjustDecimalPlace(n,p-1-e);}}var int;if(e>=p-1){m=m+repeat('0',e-p+1);int=e+1;}else if(e>=0){m="".concat(m.slice(0,e+1),".").concat(m.slice(e+1));int=e+1;}else {m="0.".concat(repeat('0',-e-1)).concat(m);int=1;}if(m.indexOf('.')>=0&&maxPrecision>minPrecision){var cut=maxPrecision-minPrecision;while(cut>0&&m[m.length-1]==='0'){m=m.slice(0,-1);cut--;}if(m[m.length-1]==='.'){m=m.slice(0,-1);}}return {formattedString:m,roundedNumber:xFinal,integerDigitsCount:int};// x / (10 ** magnitude), but try to preserve as much floating point precision as possible.
function adjustDecimalPlace(x,magnitude){return magnitude<0?x*Math.pow(10,-magnitude):x/Math.pow(10,magnitude);}}

/**
 * TODO: dedup with intl-pluralrules and support BigInt
 * https://tc39.es/ecma402/#sec-torawfixed
 * @param x a finite non-negative Number or BigInt
 * @param minFraction and integer between 0 and 20
 * @param maxFraction and integer between 0 and 20
 */function ToRawFixed(x,minFraction,maxFraction){var f=maxFraction;var n=Math.round(x*Math.pow(10,f));var xFinal=n/Math.pow(10,f);// n is a positive integer, but it is possible to be greater than 1e21.
// In such case we will go the slow path.
// See also: https://tc39.es/ecma262/#sec-numeric-types-number-tostring
var m;if(n<1e21){m=n.toString();}else {m=n.toString();var _a=m.split('e'),mantissa=_a[0],exponent=_a[1];m=mantissa.replace('.','');m=m+repeat('0',Math.max(+exponent-m.length+1,0));}var int;if(f!==0){var k=m.length;if(k<=f){var z=repeat('0',f+1-k);m=z+m;k=f+1;}var a=m.slice(0,k-f);var b=m.slice(k-f);m="".concat(a,".").concat(b);int=a.length;}else {int=m.length;}var cut=maxFraction-minFraction;while(cut>0&&m[m.length-1]==='0'){m=m.slice(0,-1);cut--;}if(m[m.length-1]==='.'){m=m.slice(0,-1);}return {formattedString:m,roundedNumber:xFinal,integerDigitsCount:int};}

/**
 * https://tc39.es/ecma402/#sec-formatnumberstring
 */function FormatNumericToString(intlObject,x){var isNegative=x<0||SameValue(x,-0);if(isNegative){x=-x;}var result;var rourndingType=intlObject.roundingType;switch(rourndingType){case'significantDigits':result=ToRawPrecision(x,intlObject.minimumSignificantDigits,intlObject.maximumSignificantDigits);break;case'fractionDigits':result=ToRawFixed(x,intlObject.minimumFractionDigits,intlObject.maximumFractionDigits);break;default:result=ToRawPrecision(x,1,2);if(result.integerDigitsCount>1){result=ToRawFixed(x,0,0);}break;}x=result.roundedNumber;var string=result.formattedString;var int=result.integerDigitsCount;var minInteger=intlObject.minimumIntegerDigits;if(int<minInteger){var forwardZeros=repeat('0',minInteger-int);string=forwardZeros+string;}if(isNegative){x=-x;}return {roundedNumber:x,formattedString:string};}

/**
 * The abstract operation ComputeExponent computes an exponent (power of ten) by which to scale x
 * according to the number formatting settings. It handles cases such as 999 rounding up to 1000,
 * requiring a different exponent.
 *
 * NOT IN SPEC: it returns [exponent, magnitude].
 */function ComputeExponent(numberFormat,x,_a){var getInternalSlots=_a.getInternalSlots;if(x===0){return [0,0];}if(x<0){x=-x;}var magnitude=getMagnitude(x);var exponent=ComputeExponentForMagnitude(numberFormat,magnitude,{getInternalSlots:getInternalSlots});// Preserve more precision by doing multiplication when exponent is negative.
x=exponent<0?x*Math.pow(10,-exponent):x/Math.pow(10,exponent);var formatNumberResult=FormatNumericToString(getInternalSlots(numberFormat),x);if(formatNumberResult.roundedNumber===0){return [exponent,magnitude];}var newMagnitude=getMagnitude(formatNumberResult.roundedNumber);if(newMagnitude===magnitude-exponent){return [exponent,magnitude];}return [ComputeExponentForMagnitude(numberFormat,magnitude+1,{getInternalSlots:getInternalSlots}),magnitude+1];}

/**
 * https://tc39.es/ecma402/#sec-currencydigits
 */function CurrencyDigits(c,_a){var currencyDigitsData=_a.currencyDigitsData;return HasOwnProperty(currencyDigitsData,c)?currencyDigitsData[c]:2;}

var digitMapping={"adlm":["𞥐","𞥑","𞥒","𞥓","𞥔","𞥕","𞥖","𞥗","𞥘","𞥙"],"ahom":["𑜰","𑜱","𑜲","𑜳","𑜴","𑜵","𑜶","𑜷","𑜸","𑜹"],"arab":["٠","١","٢","٣","٤","٥","٦","٧","٨","٩"],"arabext":["۰","۱","۲","۳","۴","۵","۶","۷","۸","۹"],"bali":["᭐","᭑","᭒","᭓","᭔","᭕","᭖","᭗","᭘","᭙"],"beng":["০","১","২","৩","৪","৫","৬","৭","৮","৯"],"bhks":["𑱐","𑱑","𑱒","𑱓","𑱔","𑱕","𑱖","𑱗","𑱘","𑱙"],"brah":["𑁦","𑁧","𑁨","𑁩","𑁪","𑁫","𑁬","𑁭","𑁮","𑁯"],"cakm":["𑄶","𑄷","𑄸","𑄹","𑄺","𑄻","𑄼","𑄽","𑄾","𑄿"],"cham":["꩐","꩑","꩒","꩓","꩔","꩕","꩖","꩗","꩘","꩙"],"deva":["०","१","२","३","४","५","६","७","८","९"],"diak":["𑥐","𑥑","𑥒","𑥓","𑥔","𑥕","𑥖","𑥗","𑥘","𑥙"],"fullwide":["０","１","２","３","４","５","６","７","８","９"],"gong":["𑶠","𑶡","𑶢","𑶣","𑶤","𑶥","𑶦","𑶧","𑶨","𑶩"],"gonm":["𑵐","𑵑","𑵒","𑵓","𑵔","𑵕","𑵖","𑵗","𑵘","𑵙"],"gujr":["૦","૧","૨","૩","૪","૫","૬","૭","૮","૯"],"guru":["੦","੧","੨","੩","੪","੫","੬","੭","੮","੯"],"hanidec":["〇","一","二","三","四","五","六","七","八","九"],"hmng":["𖭐","𖭑","𖭒","𖭓","𖭔","𖭕","𖭖","𖭗","𖭘","𖭙"],"hmnp":["𞅀","𞅁","𞅂","𞅃","𞅄","𞅅","𞅆","𞅇","𞅈","𞅉"],"java":["꧐","꧑","꧒","꧓","꧔","꧕","꧖","꧗","꧘","꧙"],"kali":["꤀","꤁","꤂","꤃","꤄","꤅","꤆","꤇","꤈","꤉"],"khmr":["០","១","២","៣","៤","៥","៦","៧","៨","៩"],"knda":["೦","೧","೨","೩","೪","೫","೬","೭","೮","೯"],"lana":["᪀","᪁","᪂","᪃","᪄","᪅","᪆","᪇","᪈","᪉"],"lanatham":["᪐","᪑","᪒","᪓","᪔","᪕","᪖","᪗","᪘","᪙"],"laoo":["໐","໑","໒","໓","໔","໕","໖","໗","໘","໙"],"lepc":["᪐","᪑","᪒","᪓","᪔","᪕","᪖","᪗","᪘","᪙"],"limb":["᥆","᥇","᥈","᥉","᥊","᥋","᥌","᥍","᥎","᥏"],"mathbold":["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"],"mathdbl":["𝟘","𝟙","𝟚","𝟛","𝟜","𝟝","𝟞","𝟟","𝟠","𝟡"],"mathmono":["𝟶","𝟷","𝟸","𝟹","𝟺","𝟻","𝟼","𝟽","𝟾","𝟿"],"mathsanb":["𝟬","𝟭","𝟮","𝟯","𝟰","𝟱","𝟲","𝟳","𝟴","𝟵"],"mathsans":["𝟢","𝟣","𝟤","𝟥","𝟦","𝟧","𝟨","𝟩","𝟪","𝟫"],"mlym":["൦","൧","൨","൩","൪","൫","൬","൭","൮","൯"],"modi":["𑙐","𑙑","𑙒","𑙓","𑙔","𑙕","𑙖","𑙗","𑙘","𑙙"],"mong":["᠐","᠑","᠒","᠓","᠔","᠕","᠖","᠗","᠘","᠙"],"mroo":["𖩠","𖩡","𖩢","𖩣","𖩤","𖩥","𖩦","𖩧","𖩨","𖩩"],"mtei":["꯰","꯱","꯲","꯳","꯴","꯵","꯶","꯷","꯸","꯹"],"mymr":["၀","၁","၂","၃","၄","၅","၆","၇","၈","၉"],"mymrshan":["႐","႑","႒","႓","႔","႕","႖","႗","႘","႙"],"mymrtlng":["꧰","꧱","꧲","꧳","꧴","꧵","꧶","꧷","꧸","꧹"],"newa":["𑑐","𑑑","𑑒","𑑓","𑑔","𑑕","𑑖","𑑗","𑑘","𑑙"],"nkoo":["߀","߁","߂","߃","߄","߅","߆","߇","߈","߉"],"olck":["᱐","᱑","᱒","᱓","᱔","᱕","᱖","᱗","᱘","᱙"],"orya":["୦","୧","୨","୩","୪","୫","୬","୭","୮","୯"],"osma":["𐒠","𐒡","𐒢","𐒣","𐒤","𐒥","𐒦","𐒧","𐒨","𐒩"],"rohg":["𐴰","𐴱","𐴲","𐴳","𐴴","𐴵","𐴶","𐴷","𐴸","𐴹"],"saur":["꣐","꣑","꣒","꣓","꣔","꣕","꣖","꣗","꣘","꣙"],"segment":["🯰","🯱","🯲","🯳","🯴","🯵","🯶","🯷","🯸","🯹"],"shrd":["𑇐","𑇑","𑇒","𑇓","𑇔","𑇕","𑇖","𑇗","𑇘","𑇙"],"sind":["𑋰","𑋱","𑋲","𑋳","𑋴","𑋵","𑋶","𑋷","𑋸","𑋹"],"sinh":["෦","෧","෨","෩","෪","෫","෬","෭","෮","෯"],"sora":["𑃰","𑃱","𑃲","𑃳","𑃴","𑃵","𑃶","𑃷","𑃸","𑃹"],"sund":["᮰","᮱","᮲","᮳","᮴","᮵","᮶","᮷","᮸","᮹"],"takr":["𑛀","𑛁","𑛂","𑛃","𑛄","𑛅","𑛆","𑛇","𑛈","𑛉"],"talu":["᧐","᧑","᧒","᧓","᧔","᧕","᧖","᧗","᧘","᧙"],"tamldec":["௦","௧","௨","௩","௪","௫","௬","௭","௮","௯"],"telu":["౦","౧","౨","౩","౪","౫","౬","౭","౮","౯"],"thai":["๐","๑","๒","๓","๔","๕","๖","๗","๘","๙"],"tibt":["༠","༡","༢","༣","༤","༥","༦","༧","༨","༩"],"tirh":["𑓐","𑓑","𑓒","𑓓","𑓔","𑓕","𑓖","𑓗","𑓘","𑓙"],"vaii":["ᘠ","ᘡ","ᘢ","ᘣ","ᘤ","ᘥ","ᘦ","ᘧ","ᘨ","ᘩ"],"wara":["𑣠","𑣡","𑣢","𑣣","𑣤","𑣥","𑣦","𑣧","𑣨","𑣩"],"wcho":["𞋰","𞋱","𞋲","𞋳","𞋴","𞋵","𞋶","𞋷","𞋸","𞋹"]};

// @generated from regex-gen.ts
var S_UNICODE_REGEX=/[\$\+<->\^`\|~\xA2-\xA6\xA8\xA9\xAC\xAE-\xB1\xB4\xB8\xD7\xF7\u02C2-\u02C5\u02D2-\u02DF\u02E5-\u02EB\u02ED\u02EF-\u02FF\u0375\u0384\u0385\u03F6\u0482\u058D-\u058F\u0606-\u0608\u060B\u060E\u060F\u06DE\u06E9\u06FD\u06FE\u07F6\u07FE\u07FF\u09F2\u09F3\u09FA\u09FB\u0AF1\u0B70\u0BF3-\u0BFA\u0C7F\u0D4F\u0D79\u0E3F\u0F01-\u0F03\u0F13\u0F15-\u0F17\u0F1A-\u0F1F\u0F34\u0F36\u0F38\u0FBE-\u0FC5\u0FC7-\u0FCC\u0FCE\u0FCF\u0FD5-\u0FD8\u109E\u109F\u1390-\u1399\u166D\u17DB\u1940\u19DE-\u19FF\u1B61-\u1B6A\u1B74-\u1B7C\u1FBD\u1FBF-\u1FC1\u1FCD-\u1FCF\u1FDD-\u1FDF\u1FED-\u1FEF\u1FFD\u1FFE\u2044\u2052\u207A-\u207C\u208A-\u208C\u20A0-\u20BF\u2100\u2101\u2103-\u2106\u2108\u2109\u2114\u2116-\u2118\u211E-\u2123\u2125\u2127\u2129\u212E\u213A\u213B\u2140-\u2144\u214A-\u214D\u214F\u218A\u218B\u2190-\u2307\u230C-\u2328\u232B-\u2426\u2440-\u244A\u249C-\u24E9\u2500-\u2767\u2794-\u27C4\u27C7-\u27E5\u27F0-\u2982\u2999-\u29D7\u29DC-\u29FB\u29FE-\u2B73\u2B76-\u2B95\u2B97-\u2BFF\u2CE5-\u2CEA\u2E50\u2E51\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u2FF0-\u2FFB\u3004\u3012\u3013\u3020\u3036\u3037\u303E\u303F\u309B\u309C\u3190\u3191\u3196-\u319F\u31C0-\u31E3\u3200-\u321E\u322A-\u3247\u3250\u3260-\u327F\u328A-\u32B0\u32C0-\u33FF\u4DC0-\u4DFF\uA490-\uA4C6\uA700-\uA716\uA720\uA721\uA789\uA78A\uA828-\uA82B\uA836-\uA839\uAA77-\uAA79\uAB5B\uAB6A\uAB6B\uFB29\uFBB2-\uFBC1\uFDFC\uFDFD\uFE62\uFE64-\uFE66\uFE69\uFF04\uFF0B\uFF1C-\uFF1E\uFF3E\uFF40\uFF5C\uFF5E\uFFE0-\uFFE6\uFFE8-\uFFEE\uFFFC\uFFFD]|\uD800[\uDD37-\uDD3F\uDD79-\uDD89\uDD8C-\uDD8E\uDD90-\uDD9C\uDDA0\uDDD0-\uDDFC]|\uD802[\uDC77\uDC78\uDEC8]|\uD805\uDF3F|\uD807[\uDFD5-\uDFF1]|\uD81A[\uDF3C-\uDF3F\uDF45]|\uD82F\uDC9C|\uD834[\uDC00-\uDCF5\uDD00-\uDD26\uDD29-\uDD64\uDD6A-\uDD6C\uDD83\uDD84\uDD8C-\uDDA9\uDDAE-\uDDE8\uDE00-\uDE41\uDE45\uDF00-\uDF56]|\uD835[\uDEC1\uDEDB\uDEFB\uDF15\uDF35\uDF4F\uDF6F\uDF89\uDFA9\uDFC3]|\uD836[\uDC00-\uDDFF\uDE37-\uDE3A\uDE6D-\uDE74\uDE76-\uDE83\uDE85\uDE86]|\uD838[\uDD4F\uDEFF]|\uD83B[\uDCAC\uDCB0\uDD2E\uDEF0\uDEF1]|\uD83C[\uDC00-\uDC2B\uDC30-\uDC93\uDCA0-\uDCAE\uDCB1-\uDCBF\uDCC1-\uDCCF\uDCD1-\uDCF5\uDD0D-\uDDAD\uDDE6-\uDE02\uDE10-\uDE3B\uDE40-\uDE48\uDE50\uDE51\uDE60-\uDE65\uDF00-\uDFFF]|\uD83D[\uDC00-\uDED7\uDEE0-\uDEEC\uDEF0-\uDEFC\uDF00-\uDF73\uDF80-\uDFD8\uDFE0-\uDFEB]|\uD83E[\uDC00-\uDC0B\uDC10-\uDC47\uDC50-\uDC59\uDC60-\uDC87\uDC90-\uDCAD\uDCB0\uDCB1\uDD00-\uDD78\uDD7A-\uDDCB\uDDCD-\uDE53\uDE60-\uDE6D\uDE70-\uDE74\uDE78-\uDE7A\uDE80-\uDE86\uDE90-\uDEA8\uDEB0-\uDEB6\uDEC0-\uDEC2\uDED0-\uDED6\uDF00-\uDF92\uDF94-\uDFCA]/;

// IE11 does not support unicode flag, otherwise this is just /\p{S}/u.
// /^\p{S}/u
var CARET_S_UNICODE_REGEX=new RegExp("^".concat(S_UNICODE_REGEX.source));// /\p{S}$/u
var S_DOLLAR_UNICODE_REGEX=new RegExp("".concat(S_UNICODE_REGEX.source,"$"));var CLDR_NUMBER_PATTERN=/[#0](?:[\.,][#0]+)*/g;function formatToParts(numberResult,data,pl,options){var sign=numberResult.sign,exponent=numberResult.exponent,magnitude=numberResult.magnitude;var notation=options.notation,style=options.style,numberingSystem=options.numberingSystem;var defaultNumberingSystem=data.numbers.nu[0];// #region Part 1: partition and interpolate the CLDR number pattern.
// ----------------------------------------------------------
var compactNumberPattern=null;if(notation==='compact'&&magnitude){compactNumberPattern=getCompactDisplayPattern(numberResult,pl,data,style,options.compactDisplay,options.currencyDisplay,numberingSystem);}// This is used multiple times
var nonNameCurrencyPart;if(style==='currency'&&options.currencyDisplay!=='name'){var byCurrencyDisplay=data.currencies[options.currency];if(byCurrencyDisplay){switch(options.currencyDisplay){case'code':nonNameCurrencyPart=options.currency;break;case'symbol':nonNameCurrencyPart=byCurrencyDisplay.symbol;break;default:nonNameCurrencyPart=byCurrencyDisplay.narrow;break;}}else {// Fallback for unknown currency
nonNameCurrencyPart=options.currency;}}var numberPattern;if(!compactNumberPattern){// Note: if the style is unit, or is currency and the currency display is name,
// its unit parts will be interpolated in part 2. So here we can fallback to decimal.
if(style==='decimal'||style==='unit'||style==='currency'&&options.currencyDisplay==='name'){// Shortcut for decimal
var decimalData=data.numbers.decimal[numberingSystem]||data.numbers.decimal[defaultNumberingSystem];numberPattern=getPatternForSign(decimalData.standard,sign);}else if(style==='currency'){var currencyData=data.numbers.currency[numberingSystem]||data.numbers.currency[defaultNumberingSystem];// We replace number pattern part with `0` for easier postprocessing.
numberPattern=getPatternForSign(currencyData[options.currencySign],sign);}else {// percent
var percentPattern=data.numbers.percent[numberingSystem]||data.numbers.percent[defaultNumberingSystem];numberPattern=getPatternForSign(percentPattern,sign);}}else {numberPattern=compactNumberPattern;}// Extract the decimal number pattern string. It looks like "#,##0,00", which will later be
// used to infer decimal group sizes.
var decimalNumberPattern=CLDR_NUMBER_PATTERN.exec(numberPattern)[0];// Now we start to substitute patterns
// 1. replace strings like `0` and `#,##0.00` with `{0}`
// 2. unquote characters (invariant: the quoted characters does not contain the special tokens)
numberPattern=numberPattern.replace(CLDR_NUMBER_PATTERN,'{0}').replace(/'(.)'/g,'$1');// Handle currency spacing (both compact and non-compact).
if(style==='currency'&&options.currencyDisplay!=='name'){var currencyData=data.numbers.currency[numberingSystem]||data.numbers.currency[defaultNumberingSystem];// See `currencySpacing` substitution rule in TR-35.
// Here we always assume the currencyMatch is "[:^S:]" and surroundingMatch is "[:digit:]".
//
// Example 1: for pattern "#,##0.00¤" with symbol "US$", we replace "¤" with the symbol,
// but insert an extra non-break space before the symbol, because "[:^S:]" matches "U" in
// "US$" and "[:digit:]" matches the latn numbering system digits.
//
// Example 2: for pattern "¤#,##0.00" with symbol "US$", there is no spacing between symbol
// and number, because `$` does not match "[:^S:]".
//
// Implementation note: here we do the best effort to infer the insertion.
// We also assume that `beforeInsertBetween` and `afterInsertBetween` will never be `;`.
var afterCurrency=currencyData.currencySpacing.afterInsertBetween;if(afterCurrency&&!S_DOLLAR_UNICODE_REGEX.test(nonNameCurrencyPart)){numberPattern=numberPattern.replace('¤{0}',"\u00A4".concat(afterCurrency,"{0}"));}var beforeCurrency=currencyData.currencySpacing.beforeInsertBetween;if(beforeCurrency&&!CARET_S_UNICODE_REGEX.test(nonNameCurrencyPart)){numberPattern=numberPattern.replace('{0}¤',"{0}".concat(beforeCurrency,"\u00A4"));}}// The following tokens are special: `{0}`, `¤`, `%`, `-`, `+`, `{c:...}.
var numberPatternParts=numberPattern.split(/({c:[^}]+}|\{0\}|[¤%\-\+])/g);var numberParts=[];var symbols=data.numbers.symbols[numberingSystem]||data.numbers.symbols[defaultNumberingSystem];for(var _i=0,numberPatternParts_1=numberPatternParts;_i<numberPatternParts_1.length;_i++){var part=numberPatternParts_1[_i];if(!part){continue;}switch(part){case'{0}':{// We only need to handle scientific and engineering notation here.
numberParts.push.apply(numberParts,paritionNumberIntoParts(symbols,numberResult,notation,exponent,numberingSystem,// If compact number pattern exists, do not insert group separators.
!compactNumberPattern&&options.useGrouping,decimalNumberPattern));break;}case'-':numberParts.push({type:'minusSign',value:symbols.minusSign});break;case'+':numberParts.push({type:'plusSign',value:symbols.plusSign});break;case'%':numberParts.push({type:'percentSign',value:symbols.percentSign});break;case'¤':// Computed above when handling currency spacing.
numberParts.push({type:'currency',value:nonNameCurrencyPart});break;default:if(/^\{c:/.test(part)){numberParts.push({type:'compact',value:part.substring(3,part.length-1)});}else {// literal
numberParts.push({type:'literal',value:part});}break;}}// #endregion
// #region Part 2: interpolate unit pattern if necessary.
// ----------------------------------------------
switch(style){case'currency':{// `currencyDisplay: 'name'` has similar pattern handling as units.
if(options.currencyDisplay==='name'){var unitPattern=(data.numbers.currency[numberingSystem]||data.numbers.currency[defaultNumberingSystem]).unitPattern;// Select plural
var unitName=void 0;var currencyNameData=data.currencies[options.currency];if(currencyNameData){unitName=selectPlural(pl,numberResult.roundedNumber*Math.pow(10,exponent),currencyNameData.displayName);}else {// Fallback for unknown currency
unitName=options.currency;}// Do {0} and {1} substitution
var unitPatternParts=unitPattern.split(/(\{[01]\})/g);var result=[];for(var _a=0,unitPatternParts_1=unitPatternParts;_a<unitPatternParts_1.length;_a++){var part=unitPatternParts_1[_a];switch(part){case'{0}':result.push.apply(result,numberParts);break;case'{1}':result.push({type:'currency',value:unitName});break;default:if(part){result.push({type:'literal',value:part});}break;}}return result;}else {return numberParts;}}case'unit':{var unit=options.unit,unitDisplay=options.unitDisplay;var unitData=data.units.simple[unit];var unitPattern=void 0;if(unitData){// Simple unit pattern
unitPattern=selectPlural(pl,numberResult.roundedNumber*Math.pow(10,exponent),data.units.simple[unit][unitDisplay]);}else {// See: http://unicode.org/reports/tr35/tr35-general.html#perUnitPatterns
// If cannot find unit in the simple pattern, it must be "per" compound pattern.
// Implementation note: we are not following TR-35 here because we need to format to parts!
var _b=unit.split('-per-'),numeratorUnit=_b[0],denominatorUnit=_b[1];unitData=data.units.simple[numeratorUnit];var numeratorUnitPattern=selectPlural(pl,numberResult.roundedNumber*Math.pow(10,exponent),data.units.simple[numeratorUnit][unitDisplay]);var perUnitPattern=data.units.simple[denominatorUnit].perUnit[unitDisplay];if(perUnitPattern){// perUnitPattern exists, combine it with numeratorUnitPattern
unitPattern=perUnitPattern.replace('{0}',numeratorUnitPattern);}else {// get compoundUnit pattern (e.g. "{0} per {1}"), repalce {0} with numerator pattern and {1} with
// the denominator pattern in singular form.
var perPattern=data.units.compound.per[unitDisplay];var denominatorPattern=selectPlural(pl,1,data.units.simple[denominatorUnit][unitDisplay]);unitPattern=unitPattern=perPattern.replace('{0}',numeratorUnitPattern).replace('{1}',denominatorPattern.replace('{0}',''));}}var result=[];// We need spacing around "{0}" because they are not treated as "unit" parts, but "literal".
for(var _c=0,_d=unitPattern.split(/(\s*\{0\}\s*)/);_c<_d.length;_c++){var part=_d[_c];var interpolateMatch=/^(\s*)\{0\}(\s*)$/.exec(part);if(interpolateMatch){// Space before "{0}"
if(interpolateMatch[1]){result.push({type:'literal',value:interpolateMatch[1]});}// "{0}" itself
result.push.apply(result,numberParts);// Space after "{0}"
if(interpolateMatch[2]){result.push({type:'literal',value:interpolateMatch[2]});}}else if(part){result.push({type:'unit',value:part});}}return result;}default:return numberParts;}// #endregion
}// A subset of https://tc39.es/ecma402/#sec-partitionnotationsubpattern
// Plus the exponent parts handling.
function paritionNumberIntoParts(symbols,numberResult,notation,exponent,numberingSystem,useGrouping,/**
 * This is the decimal number pattern without signs or symbols.
 * It is used to infer the group size when `useGrouping` is true.
 *
 * A typical value looks like "#,##0.00" (primary group size is 3).
 * Some locales like Hindi has secondary group size of 2 (e.g. "#,##,##0.00").
 */decimalNumberPattern){var result=[];// eslint-disable-next-line prefer-const
var n=numberResult.formattedString,x=numberResult.roundedNumber;if(isNaN(x)){return [{type:'nan',value:n}];}else if(!isFinite(x)){return [{type:'infinity',value:n}];}var digitReplacementTable=digitMapping[numberingSystem];if(digitReplacementTable){n=n.replace(/\d/g,function(digit){return digitReplacementTable[+digit]||digit;});}// TODO: Else use an implementation dependent algorithm to map n to the appropriate
// representation of n in the given numbering system.
var decimalSepIndex=n.indexOf('.');var integer;var fraction;if(decimalSepIndex>0){integer=n.slice(0,decimalSepIndex);fraction=n.slice(decimalSepIndex+1);}else {integer=n;}// #region Grouping integer digits
// The weird compact and x >= 10000 check is to ensure consistency with Node.js and Chrome.
// Note that `de` does not have compact form for thousands, but Node.js does not insert grouping separator
// unless the rounded number is greater than 10000:
//   NumberFormat('de', {notation: 'compact', compactDisplay: 'short'}).format(1234) //=> "1234"
//   NumberFormat('de').format(1234) //=> "1.234"
if(useGrouping&&(notation!=='compact'||x>=10000)){var groupSepSymbol=symbols.group;var groups=[];// > There may be two different grouping sizes: The primary grouping size used for the least
// > significant integer group, and the secondary grouping size used for more significant groups.
// > If a pattern contains multiple grouping separators, the interval between the last one and the
// > end of the integer defines the primary grouping size, and the interval between the last two
// > defines the secondary grouping size. All others are ignored.
var integerNumberPattern=decimalNumberPattern.split('.')[0];var patternGroups=integerNumberPattern.split(',');var primaryGroupingSize=3;var secondaryGroupingSize=3;if(patternGroups.length>1){primaryGroupingSize=patternGroups[patternGroups.length-1].length;}if(patternGroups.length>2){secondaryGroupingSize=patternGroups[patternGroups.length-2].length;}var i=integer.length-primaryGroupingSize;if(i>0){// Slice the least significant integer group
groups.push(integer.slice(i,i+primaryGroupingSize));// Then iteratively push the more signicant groups
// TODO: handle surrogate pairs in some numbering system digits
for(i-=secondaryGroupingSize;i>0;i-=secondaryGroupingSize){groups.push(integer.slice(i,i+secondaryGroupingSize));}groups.push(integer.slice(0,i+secondaryGroupingSize));}else {groups.push(integer);}while(groups.length>0){var integerGroup=groups.pop();result.push({type:'integer',value:integerGroup});if(groups.length>0){result.push({type:'group',value:groupSepSymbol});}}}else {result.push({type:'integer',value:integer});}// #endregion
if(fraction!==undefined){result.push({type:'decimal',value:symbols.decimal},{type:'fraction',value:fraction});}if((notation==='scientific'||notation==='engineering')&&isFinite(x)){result.push({type:'exponentSeparator',value:symbols.exponential});if(exponent<0){result.push({type:'exponentMinusSign',value:symbols.minusSign});exponent=-exponent;}var exponentResult=ToRawFixed(exponent,0,0);result.push({type:'exponentInteger',value:exponentResult.formattedString});}return result;}function getPatternForSign(pattern,sign){if(pattern.indexOf(';')<0){pattern="".concat(pattern,";-").concat(pattern);}var _a=pattern.split(';'),zeroPattern=_a[0],negativePattern=_a[1];switch(sign){case 0:return zeroPattern;case-1:return negativePattern;default:return negativePattern.indexOf('-')>=0?negativePattern.replace(/-/g,'+'):"+".concat(zeroPattern);}}// Find the CLDR pattern for compact notation based on the magnitude of data and style.
//
// Example return value: "¤ {c:laki}000;¤{c:laki} -0" (`sw` locale):
// - Notice the `{c:...}` token that wraps the compact literal.
// - The consecutive zeros are normalized to single zero to match CLDR_NUMBER_PATTERN.
//
// Returning null means the compact display pattern cannot be found.
function getCompactDisplayPattern(numberResult,pl,data,style,compactDisplay,currencyDisplay,numberingSystem){var _a;var roundedNumber=numberResult.roundedNumber,sign=numberResult.sign,magnitude=numberResult.magnitude;var magnitudeKey=String(Math.pow(10,magnitude));var defaultNumberingSystem=data.numbers.nu[0];var pattern;if(style==='currency'&&currencyDisplay!=='name'){var byNumberingSystem=data.numbers.currency;var currencyData=byNumberingSystem[numberingSystem]||byNumberingSystem[defaultNumberingSystem];// NOTE: compact notation ignores currencySign!
var compactPluralRules=(_a=currencyData.short)===null||_a===void 0?void 0:_a[magnitudeKey];if(!compactPluralRules){return null;}pattern=selectPlural(pl,roundedNumber,compactPluralRules);}else {var byNumberingSystem=data.numbers.decimal;var byCompactDisplay=byNumberingSystem[numberingSystem]||byNumberingSystem[defaultNumberingSystem];var compactPlaralRule=byCompactDisplay[compactDisplay][magnitudeKey];if(!compactPlaralRule){return null;}pattern=selectPlural(pl,roundedNumber,compactPlaralRule);}// See https://unicode.org/reports/tr35/tr35-numbers.html#Compact_Number_Formats
// > If the value is precisely “0”, either explicit or defaulted, then the normal number format
// > pattern for that sort of object is supplied.
if(pattern==='0'){return null;}pattern=getPatternForSign(pattern,sign)// Extract compact literal from the pattern
.replace(/([^\s;\-\+\d¤]+)/g,'{c:$1}')// We replace one or more zeros with a single zero so it matches `CLDR_NUMBER_PATTERN`.
.replace(/0+/,'0');return pattern;}function selectPlural(pl,x,rules){return rules[pl.select(x)]||rules.other;}

/**
 * https://tc39.es/ecma402/#sec-formatnumberstring
 */function PartitionNumberPattern(numberFormat,x,_a){var _b;var getInternalSlots=_a.getInternalSlots;var internalSlots=getInternalSlots(numberFormat);var pl=internalSlots.pl,dataLocaleData=internalSlots.dataLocaleData,numberingSystem=internalSlots.numberingSystem;var symbols=dataLocaleData.numbers.symbols[numberingSystem]||dataLocaleData.numbers.symbols[dataLocaleData.numbers.nu[0]];var magnitude=0;var exponent=0;var n;if(isNaN(x)){n=symbols.nan;}else if(!isFinite(x)){n=symbols.infinity;}else {if(internalSlots.style==='percent'){x*=100;}_b=ComputeExponent(numberFormat,x,{getInternalSlots:getInternalSlots}),exponent=_b[0],magnitude=_b[1];// Preserve more precision by doing multiplication when exponent is negative.
x=exponent<0?x*Math.pow(10,-exponent):x/Math.pow(10,exponent);var formatNumberResult=FormatNumericToString(internalSlots,x);n=formatNumberResult.formattedString;x=formatNumberResult.roundedNumber;}// Based on https://tc39.es/ecma402/#sec-getnumberformatpattern
// We need to do this before `x` is rounded.
var sign;var signDisplay=internalSlots.signDisplay;switch(signDisplay){case'never':sign=0;break;case'auto':if(SameValue(x,0)||x>0||isNaN(x)){sign=0;}else {sign=-1;}break;case'always':if(SameValue(x,0)||x>0||isNaN(x)){sign=1;}else {sign=-1;}break;default:// x === 0 -> x is 0 or x is -0
if(x===0||isNaN(x)){sign=0;}else if(x>0){sign=1;}else {sign=-1;}}return formatToParts({roundedNumber:x,formattedString:n,exponent:exponent,magnitude:magnitude,sign:sign},internalSlots.dataLocaleData,pl,internalSlots);}

function FormatNumericToParts(nf,x,implDetails){var parts=PartitionNumberPattern(nf,x,implDetails);var result=ArrayCreate(0);for(var _i=0,parts_1=parts;_i<parts_1.length;_i++){var part=parts_1[_i];result.push({type:part.type,value:part.value});}return result;}

/**
 * https://tc39.es/ecma402/#sec-setnumberformatunitoptions
 */function SetNumberFormatUnitOptions(nf,options,_a){if(options===void 0){options=Object.create(null);}var getInternalSlots=_a.getInternalSlots;var internalSlots=getInternalSlots(nf);var style=GetOption(options,'style','string',['decimal','percent','currency','unit'],'decimal');internalSlots.style=style;var currency=GetOption(options,'currency','string',undefined,undefined);if(currency!==undefined&&!IsWellFormedCurrencyCode(currency)){throw RangeError('Malformed currency code');}if(style==='currency'&&currency===undefined){throw TypeError('currency cannot be undefined');}var currencyDisplay=GetOption(options,'currencyDisplay','string',['code','symbol','narrowSymbol','name'],'symbol');var currencySign=GetOption(options,'currencySign','string',['standard','accounting'],'standard');var unit=GetOption(options,'unit','string',undefined,undefined);if(unit!==undefined&&!IsWellFormedUnitIdentifier(unit)){throw RangeError('Invalid unit argument for Intl.NumberFormat()');}if(style==='unit'&&unit===undefined){throw TypeError('unit cannot be undefined');}var unitDisplay=GetOption(options,'unitDisplay','string',['short','narrow','long'],'short');if(style==='currency'){internalSlots.currency=currency.toUpperCase();internalSlots.currencyDisplay=currencyDisplay;internalSlots.currencySign=currencySign;}if(style==='unit'){internalSlots.unit=unit;internalSlots.unitDisplay=unitDisplay;}}

/**
 * https://tc39.es/ecma402/#sec-setnfdigitoptions
 */function SetNumberFormatDigitOptions(internalSlots,opts,mnfdDefault,mxfdDefault,notation){var mnid=GetNumberOption(opts,'minimumIntegerDigits',1,21,1);var mnfd=opts.minimumFractionDigits;var mxfd=opts.maximumFractionDigits;var mnsd=opts.minimumSignificantDigits;var mxsd=opts.maximumSignificantDigits;internalSlots.minimumIntegerDigits=mnid;if(mnsd!==undefined||mxsd!==undefined){internalSlots.roundingType='significantDigits';mnsd=DefaultNumberOption(mnsd,1,21,1);mxsd=DefaultNumberOption(mxsd,mnsd,21,21);internalSlots.minimumSignificantDigits=mnsd;internalSlots.maximumSignificantDigits=mxsd;}else if(mnfd!==undefined||mxfd!==undefined){internalSlots.roundingType='fractionDigits';mnfd=DefaultNumberOption(mnfd,0,20,mnfdDefault);var mxfdActualDefault=Math.max(mnfd,mxfdDefault);mxfd=DefaultNumberOption(mxfd,mnfd,20,mxfdActualDefault);internalSlots.minimumFractionDigits=mnfd;internalSlots.maximumFractionDigits=mxfd;}else if(notation==='compact'){internalSlots.roundingType='compactRounding';}else {internalSlots.roundingType='fractionDigits';internalSlots.minimumFractionDigits=mnfdDefault;internalSlots.maximumFractionDigits=mxfdDefault;}}

/**
 * https://tc39.es/ecma402/#sec-initializenumberformat
 */function InitializeNumberFormat(nf,locales,opts,_a){var getInternalSlots=_a.getInternalSlots,localeData=_a.localeData,availableLocales=_a.availableLocales,numberingSystemNames=_a.numberingSystemNames,getDefaultLocale=_a.getDefaultLocale,currencyDigitsData=_a.currencyDigitsData;// @ts-ignore
var requestedLocales=CanonicalizeLocaleList(locales);var options=CoerceOptionsToObject(opts);var opt=Object.create(null);var matcher=GetOption(options,'localeMatcher','string',['lookup','best fit'],'best fit');opt.localeMatcher=matcher;var numberingSystem=GetOption(options,'numberingSystem','string',undefined,undefined);if(numberingSystem!==undefined&&numberingSystemNames.indexOf(numberingSystem)<0){// 8.a. If numberingSystem does not match the Unicode Locale Identifier type nonterminal,
// throw a RangeError exception.
throw RangeError("Invalid numberingSystems: ".concat(numberingSystem));}opt.nu=numberingSystem;var r=intlLocalematcher_1(availableLocales,requestedLocales,opt,// [[RelevantExtensionKeys]] slot, which is a constant
['nu'],localeData,getDefaultLocale);var dataLocaleData=localeData[r.dataLocale];invariant(!!dataLocaleData,"Missing locale data for ".concat(r.dataLocale));var internalSlots=getInternalSlots(nf);internalSlots.locale=r.locale;internalSlots.dataLocale=r.dataLocale;internalSlots.numberingSystem=r.nu;internalSlots.dataLocaleData=dataLocaleData;SetNumberFormatUnitOptions(nf,options,{getInternalSlots:getInternalSlots});var style=internalSlots.style;var mnfdDefault;var mxfdDefault;if(style==='currency'){var currency=internalSlots.currency;var cDigits=CurrencyDigits(currency,{currencyDigitsData:currencyDigitsData});mnfdDefault=cDigits;mxfdDefault=cDigits;}else {mnfdDefault=0;mxfdDefault=style==='percent'?0:3;}var notation=GetOption(options,'notation','string',['standard','scientific','engineering','compact'],'standard');internalSlots.notation=notation;SetNumberFormatDigitOptions(internalSlots,options,mnfdDefault,mxfdDefault,notation);var compactDisplay=GetOption(options,'compactDisplay','string',['short','long'],'short');if(notation==='compact'){internalSlots.compactDisplay=compactDisplay;}var useGrouping=GetOption(options,'useGrouping','boolean',undefined,true);internalSlots.useGrouping=useGrouping;var signDisplay=GetOption(options,'signDisplay','string',['auto','never','always','exceptZero'],'auto');internalSlots.signDisplay=signDisplay;return nf;}

/**
 * https://tc39.es/ecma402/#sec-partitionpattern
 * @param pattern
 */function PartitionPattern(pattern){var result=[];var beginIndex=pattern.indexOf('{');var endIndex=0;var nextIndex=0;var length=pattern.length;while(beginIndex<pattern.length&&beginIndex>-1){endIndex=pattern.indexOf('}',beginIndex);invariant(endIndex>beginIndex,"Invalid pattern ".concat(pattern));if(beginIndex>nextIndex){result.push({type:'literal',value:pattern.substring(nextIndex,beginIndex)});}result.push({type:pattern.substring(beginIndex+1,endIndex),value:undefined});nextIndex=endIndex+1;beginIndex=pattern.indexOf('{',nextIndex);}if(nextIndex<length){result.push({type:'literal',value:pattern.substring(nextIndex,length)});}return result;}

/**
 * https://tc39.es/ecma402/#sec-supportedlocales
 * @param availableLocales
 * @param requestedLocales
 * @param options
 */function SupportedLocales(availableLocales,requestedLocales,options){var matcher='best fit';if(options!==undefined){options=ToObject(options);matcher=GetOption(options,'localeMatcher','string',['lookup','best fit'],'best fit');}if(matcher==='best fit'){return intlLocalematcher_2(availableLocales,requestedLocales);}return intlLocalematcher_2(availableLocales,requestedLocales);}

/** @class */(function(_super){__extends(MissingLocaleDataError,_super);function MissingLocaleDataError(){var _this=_super!==null&&_super.apply(this,arguments)||this;_this.type='MISSING_LOCALE_DATA';return _this;}return MissingLocaleDataError;})(Error);function isMissingLocaleDataError(e){return e.type==='MISSING_LOCALE_DATA';}

var RangePatternType;(function(RangePatternType){RangePatternType["startRange"]="startRange";RangePatternType["shared"]="shared";RangePatternType["endRange"]="endRange";})(RangePatternType||(RangePatternType={}));

var lib = /*#__PURE__*/Object.freeze({
    __proto__: null,
    _formatToParts: formatToParts,
    getInternalSlot: getInternalSlot,
    getMultiInternalSlots: getMultiInternalSlots,
    isLiteralPart: isLiteralPart,
    setInternalSlot: setInternalSlot,
    setMultiInternalSlots: setMultiInternalSlots,
    getMagnitude: getMagnitude,
    defineProperty: defineProperty,
    isMissingLocaleDataError: isMissingLocaleDataError,
    invariant: invariant,
    CanonicalizeLocaleList: CanonicalizeLocaleList,
    CanonicalizeTimeZoneName: CanonicalizeTimeZoneName,
    CoerceOptionsToObject: CoerceOptionsToObject,
    GetNumberOption: GetNumberOption,
    GetOption: GetOption,
    GetOptionsObject: GetOptionsObject,
    SANCTIONED_UNITS: SANCTIONED_UNITS,
    removeUnitNamespace: removeUnitNamespace,
    SIMPLE_UNITS: SIMPLE_UNITS,
    IsSanctionedSimpleUnitIdentifier: IsSanctionedSimpleUnitIdentifier,
    IsValidTimeZoneName: IsValidTimeZoneName,
    IsWellFormedCurrencyCode: IsWellFormedCurrencyCode,
    IsWellFormedUnitIdentifier: IsWellFormedUnitIdentifier,
    ComputeExponent: ComputeExponent,
    ComputeExponentForMagnitude: ComputeExponentForMagnitude,
    CurrencyDigits: CurrencyDigits,
    FormatNumericToParts: FormatNumericToParts,
    FormatNumericToString: FormatNumericToString,
    InitializeNumberFormat: InitializeNumberFormat,
    PartitionNumberPattern: PartitionNumberPattern,
    SetNumberFormatDigitOptions: SetNumberFormatDigitOptions,
    SetNumberFormatUnitOptions: SetNumberFormatUnitOptions,
    ToRawFixed: ToRawFixed,
    ToRawPrecision: ToRawPrecision,
    PartitionPattern: PartitionPattern,
    SupportedLocales: SupportedLocales,
    get RangePatternType () { return RangePatternType; },
    ToString: ToString,
    ToNumber: ToNumber,
    TimeClip: TimeClip,
    ToObject: ToObject,
    SameValue: SameValue,
    ArrayCreate: ArrayCreate,
    HasOwnProperty: HasOwnProperty,
    Type: Type,
    Day: Day,
    WeekDay: WeekDay,
    DayFromYear: DayFromYear,
    TimeFromYear: TimeFromYear,
    YearFromTime: YearFromTime,
    DaysInYear: DaysInYear,
    DayWithinYear: DayWithinYear,
    InLeapYear: InLeapYear,
    MonthFromTime: MonthFromTime,
    DateFromTime: DateFromTime,
    HourFromTime: HourFromTime,
    MinFromTime: MinFromTime,
    SecFromTime: SecFromTime,
    OrdinaryHasInstance: OrdinaryHasInstance,
    msFromTime: msFromTime
});

var get_internal_slots=createCommonjsModule(function(module,exports){// eslint-disable-next-line import/no-cycle
Object.defineProperty(exports,"__esModule",{value:true});var internalSlotMap=new WeakMap();function getInternalSlots(x){var internalSlots=internalSlotMap.get(x);if(!internalSlots){internalSlots=Object.create(null);internalSlotMap.set(x,internalSlots);}return internalSlots;}exports.default=getInternalSlots;});unwrapExports(get_internal_slots);

var links=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});// @generated
// prettier-ignore
exports.default={"Africa/Asmera":"Africa/Nairobi","Africa/Timbuktu":"Africa/Abidjan","America/Argentina/ComodRivadavia":"America/Argentina/Catamarca","America/Atka":"America/Adak","America/Buenos_Aires":"America/Argentina/Buenos_Aires","America/Catamarca":"America/Argentina/Catamarca","America/Coral_Harbour":"America/Panama","America/Cordoba":"America/Argentina/Cordoba","America/Ensenada":"America/Tijuana","America/Fort_Wayne":"America/Indiana/Indianapolis","America/Godthab":"America/Nuuk","America/Indianapolis":"America/Indiana/Indianapolis","America/Jujuy":"America/Argentina/Jujuy","America/Knox_IN":"America/Indiana/Knox","America/Louisville":"America/Kentucky/Louisville","America/Mendoza":"America/Argentina/Mendoza","America/Montreal":"America/Toronto","America/Porto_Acre":"America/Rio_Branco","America/Rosario":"America/Argentina/Cordoba","America/Santa_Isabel":"America/Tijuana","America/Shiprock":"America/Denver","America/Virgin":"America/Puerto_Rico","Antarctica/South_Pole":"Pacific/Auckland","Asia/Ashkhabad":"Asia/Ashgabat","Asia/Calcutta":"Asia/Kolkata","Asia/Chongqing":"Asia/Shanghai","Asia/Chungking":"Asia/Shanghai","Asia/Dacca":"Asia/Dhaka","Asia/Harbin":"Asia/Shanghai","Asia/Kashgar":"Asia/Urumqi","Asia/Katmandu":"Asia/Kathmandu","Asia/Macao":"Asia/Macau","Asia/Rangoon":"Asia/Yangon","Asia/Saigon":"Asia/Ho_Chi_Minh","Asia/Tel_Aviv":"Asia/Jerusalem","Asia/Thimbu":"Asia/Thimphu","Asia/Ujung_Pandang":"Asia/Makassar","Asia/Ulan_Bator":"Asia/Ulaanbaatar","Atlantic/Faeroe":"Atlantic/Faroe","Atlantic/Jan_Mayen":"Europe/Oslo","Australia/ACT":"Australia/Sydney","Australia/Canberra":"Australia/Sydney","Australia/Currie":"Australia/Hobart","Australia/LHI":"Australia/Lord_Howe","Australia/NSW":"Australia/Sydney","Australia/North":"Australia/Darwin","Australia/Queensland":"Australia/Brisbane","Australia/South":"Australia/Adelaide","Australia/Tasmania":"Australia/Hobart","Australia/Victoria":"Australia/Melbourne","Australia/West":"Australia/Perth","Australia/Yancowinna":"Australia/Broken_Hill","Brazil/Acre":"America/Rio_Branco","Brazil/DeNoronha":"America/Noronha","Brazil/East":"America/Sao_Paulo","Brazil/West":"America/Manaus","Canada/Atlantic":"America/Halifax","Canada/Central":"America/Winnipeg","Canada/Eastern":"America/Toronto","Canada/Mountain":"America/Edmonton","Canada/Newfoundland":"America/St_Johns","Canada/Pacific":"America/Vancouver","Canada/Saskatchewan":"America/Regina","Canada/Yukon":"America/Whitehorse","Chile/Continental":"America/Santiago","Chile/EasterIsland":"Pacific/Easter","Cuba":"America/Havana","Egypt":"Africa/Cairo","Eire":"Europe/Dublin","Etc/UCT":"Etc/UTC","Europe/Belfast":"Europe/London","Europe/Tiraspol":"Europe/Chisinau","GB":"Europe/London","GB-Eire":"Europe/London","GMT+0":"Etc/GMT","GMT-0":"Etc/GMT","GMT0":"Etc/GMT","Greenwich":"Etc/GMT","Hongkong":"Asia/Hong_Kong","Iceland":"Atlantic/Reykjavik","Iran":"Asia/Tehran","Israel":"Asia/Jerusalem","Jamaica":"America/Jamaica","Japan":"Asia/Tokyo","Kwajalein":"Pacific/Kwajalein","Libya":"Africa/Tripoli","Mexico/BajaNorte":"America/Tijuana","Mexico/BajaSur":"America/Mazatlan","Mexico/General":"America/Mexico_City","NZ":"Pacific/Auckland","NZ-CHAT":"Pacific/Chatham","Navajo":"America/Denver","PRC":"Asia/Shanghai","Pacific/Enderbury":"Pacific/Kanton","Pacific/Johnston":"Pacific/Honolulu","Pacific/Ponape":"Pacific/Pohnpei","Pacific/Samoa":"Pacific/Pago_Pago","Pacific/Truk":"Pacific/Chuuk","Pacific/Yap":"Pacific/Chuuk","Poland":"Europe/Warsaw","Portugal":"Europe/Lisbon","ROC":"Asia/Taipei","ROK":"Asia/Seoul","Singapore":"Asia/Singapore","Turkey":"Europe/Istanbul","UCT":"Etc/UTC","US/Alaska":"America/Anchorage","US/Aleutian":"America/Adak","US/Arizona":"America/Phoenix","US/Central":"America/Chicago","US/East-Indiana":"America/Indiana/Indianapolis","US/Eastern":"America/New_York","US/Hawaii":"Pacific/Honolulu","US/Indiana-Starke":"America/Indiana/Knox","US/Michigan":"America/Detroit","US/Mountain":"America/Denver","US/Pacific":"America/Los_Angeles","US/Samoa":"Pacific/Pago_Pago","UTC":"Etc/UTC","Universal":"Etc/UTC","W-SU":"Europe/Moscow","Zulu":"Etc/UTC"};});unwrapExports(links);

var packer=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.unpack=exports.pack=void 0;function pack(data){var zoneNames=Object.keys(data.zones);zoneNames.sort();// so output is stable
return {zones:zoneNames.map(function(zone){return (0, tslib_es6.__spreadArray)([zone],data.zones[zone].map(function(_a){var ts=_a[0],others=_a.slice(1);return (0, tslib_es6.__spreadArray)([ts===''?'':ts.toString(36)],others,true).join(',');}),true).join('|');}),abbrvs:data.abbrvs.join('|'),offsets:data.offsets.map(function(o){return o.toString(36);}).join('|')};}exports.pack=pack;function unpack(data){var abbrvs=data.abbrvs.split('|');var offsets=data.offsets.split('|').map(function(n){return parseInt(n,36);});var packedZones=data.zones;var zones={};for(var _i=0,packedZones_1=packedZones;_i<packedZones_1.length;_i++){var d=packedZones_1[_i];var _a=d.split('|'),zone=_a[0],zoneData=_a.slice(1);zones[zone]=zoneData.map(function(z){return z.split(',');}).map(function(_a){var ts=_a[0],abbrvIndex=_a[1],offsetIndex=_a[2],dst=_a[3];return [ts===''?-Infinity:parseInt(ts,36),abbrvs[+abbrvIndex],offsets[+offsetIndex],dst==='1'];});}return zones;}exports.unpack=unpack;});unwrapExports(packer);packer.unpack;packer.pack;

var utils=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.shortMorePenalty=exports.shortLessPenalty=exports.longMorePenalty=exports.longLessPenalty=exports.differentNumericTypePenalty=exports.additionPenalty=exports.removalPenalty=exports.DATE_TIME_PROPS=void 0;exports.DATE_TIME_PROPS=['weekday','era','year','month','day','hour','minute','second','timeZoneName'];exports.removalPenalty=120;exports.additionPenalty=20;exports.differentNumericTypePenalty=15;exports.longLessPenalty=8;exports.longMorePenalty=6;exports.shortLessPenalty=6;exports.shortMorePenalty=3;});unwrapExports(utils);utils.shortMorePenalty;utils.shortLessPenalty;utils.longMorePenalty;utils.longLessPenalty;utils.differentNumericTypePenalty;utils.additionPenalty;utils.removalPenalty;utils.DATE_TIME_PROPS;

var ToLocalTime_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.ToLocalTime=void 0;function getApplicableZoneData(t,timeZone,tzData){var _a;var zoneData=tzData[timeZone];// We don't have data for this so just say it's UTC
if(!zoneData){return [0,false];}var i=0;var offset=0;var dst=false;for(;i<=zoneData.length;i++){if(i===zoneData.length||zoneData[i][0]*1e3>t){_a=zoneData[i-1],offset=_a[2],dst=_a[3];break;}}return [offset*1e3,dst];}/**
 * https://tc39.es/ecma402/#sec-tolocaltime
 * @param t
 * @param calendar
 * @param timeZone
 */function ToLocalTime(t,calendar,timeZone,_a){var tzData=_a.tzData;(0, lib.invariant)((0, lib.Type)(t)==='Number','invalid time');(0, lib.invariant)(calendar==='gregory','We only support Gregory calendar right now');var _b=getApplicableZoneData(t,timeZone,tzData),timeZoneOffset=_b[0],inDST=_b[1];var tz=t+timeZoneOffset;var year=(0, lib.YearFromTime)(tz);return {weekday:(0, lib.WeekDay)(tz),era:year<0?'BC':'AD',year:year,relatedYear:undefined,yearName:undefined,month:(0, lib.MonthFromTime)(tz),day:(0, lib.DateFromTime)(tz),hour:(0, lib.HourFromTime)(tz),minute:(0, lib.MinFromTime)(tz),second:(0, lib.SecFromTime)(tz),millisecond:(0, lib.msFromTime)(tz),inDST:inDST,// IMPORTANT: Not in spec
timeZoneOffset:timeZoneOffset};}exports.ToLocalTime=ToLocalTime;});unwrapExports(ToLocalTime_1);ToLocalTime_1.ToLocalTime;

var FormatDateTimePattern_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.FormatDateTimePattern=void 0;function pad(n){if(n<10){return "0".concat(n);}return String(n);}function offsetToGmtString(gmtFormat,hourFormat,offsetInMs,style){var offsetInMinutes=Math.floor(offsetInMs/60000);var mins=Math.abs(offsetInMinutes)%60;var hours=Math.floor(Math.abs(offsetInMinutes)/60);var _a=hourFormat.split(';'),positivePattern=_a[0],negativePattern=_a[1];var offsetStr='';var pattern=offsetInMs<0?negativePattern:positivePattern;if(style==='long'){offsetStr=pattern.replace('HH',pad(hours)).replace('H',String(hours)).replace('mm',pad(mins)).replace('m',String(mins));}else if(mins||hours){if(!mins){pattern=pattern.replace(/:?m+/,'');}offsetStr=pattern.replace(/H+/,String(hours)).replace(/m+/,String(mins));}return gmtFormat.replace('{0}',offsetStr);}/**
 * https://tc39.es/ecma402/#sec-partitiondatetimepattern
 * @param dtf
 * @param x
 */function FormatDateTimePattern(dtf,patternParts,x,_a){var getInternalSlots=_a.getInternalSlots,localeData=_a.localeData,getDefaultTimeZone=_a.getDefaultTimeZone,tzData=_a.tzData;x=(0, lib.TimeClip)(x);/** IMPL START */var internalSlots=getInternalSlots(dtf);var dataLocale=internalSlots.dataLocale;var dataLocaleData=localeData[dataLocale];/** IMPL END */var locale=internalSlots.locale;var nfOptions=Object.create(null);nfOptions.useGrouping=false;var nf=new Intl.NumberFormat(locale,nfOptions);var nf2Options=Object.create(null);nf2Options.minimumIntegerDigits=2;nf2Options.useGrouping=false;var nf2=new Intl.NumberFormat(locale,nf2Options);var fractionalSecondDigits=internalSlots.fractionalSecondDigits;var nf3;if(fractionalSecondDigits!==undefined){var nf3Options=Object.create(null);nf3Options.minimumIntegerDigits=fractionalSecondDigits;nf3Options.useGrouping=false;nf3=new Intl.NumberFormat(locale,nf3Options);}var tm=(0, ToLocalTime_1.ToLocalTime)(x,// @ts-ignore
internalSlots.calendar,internalSlots.timeZone,{tzData:tzData});var result=[];for(var _i=0,patternParts_1=patternParts;_i<patternParts_1.length;_i++){var patternPart=patternParts_1[_i];var p=patternPart.type;if(p==='literal'){result.push({type:'literal',value:patternPart.value});}else if(p==='fractionalSecondDigits'){var v=Math.floor(tm.millisecond*Math.pow(10,(fractionalSecondDigits||0)-3));result.push({// @ts-expect-error Spec is not there yet
type:'fractionalSecond',value:nf3.format(v)});}else if(p==='dayPeriod');else if(utils.DATE_TIME_PROPS.indexOf(p)>-1){var fv='';var f=internalSlots[p];// @ts-ignore
var v=tm[p];if(p==='year'&&v<=0){v=1-v;}if(p==='month'){v++;}var hourCycle=internalSlots.hourCycle;if(p==='hour'&&(hourCycle==='h11'||hourCycle==='h12')){v=v%12;if(v===0&&hourCycle==='h12'){v=12;}}if(p==='hour'&&hourCycle==='h24'){if(v===0){v=24;}}if(f==='numeric'){fv=nf.format(v);}else if(f==='2-digit'){fv=nf2.format(v);if(fv.length>2){fv=fv.slice(fv.length-2,fv.length);}}else if(f==='narrow'||f==='short'||f==='long'){if(p==='era'){fv=dataLocaleData[p][f][v];}else if(p==='timeZoneName'){var timeZoneName=dataLocaleData.timeZoneName,gmtFormat=dataLocaleData.gmtFormat,hourFormat=dataLocaleData.hourFormat;var timeZone=internalSlots.timeZone||getDefaultTimeZone();var timeZoneData=timeZoneName[timeZone];if(timeZoneData&&timeZoneData[f]){fv=timeZoneData[f][+tm.inDST];}else {// Fallback to gmtFormat
fv=offsetToGmtString(gmtFormat,hourFormat,tm.timeZoneOffset,f);}}else if(p==='month'){fv=dataLocaleData.month[f][v-1];}else {fv=dataLocaleData[p][f][v];}}result.push({type:p,value:fv});}else if(p==='ampm'){var v=tm.hour;var fv=void 0;if(v>11){fv=dataLocaleData.pm;}else {fv=dataLocaleData.am;}result.push({type:'dayPeriod',value:fv});}else if(p==='relatedYear'){var v=tm.relatedYear;// @ts-ignore
var fv=nf.format(v);result.push({// @ts-ignore TODO: Fix TS type
type:'relatedYear',value:fv});}else if(p==='yearName'){var v=tm.yearName;// @ts-ignore
var fv=nf.format(v);result.push({// @ts-ignore TODO: Fix TS type
type:'yearName',value:fv});}}return result;}exports.FormatDateTimePattern=FormatDateTimePattern;});unwrapExports(FormatDateTimePattern_1);FormatDateTimePattern_1.FormatDateTimePattern;

var PartitionDateTimePattern_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.PartitionDateTimePattern=void 0;/**
 * https://tc39.es/ecma402/#sec-partitiondatetimepattern
 * @param dtf
 * @param x
 */function PartitionDateTimePattern(dtf,x,implDetails){x=(0, lib.TimeClip)(x);if(isNaN(x)){throw new RangeError('invalid time');}/** IMPL START */var getInternalSlots=implDetails.getInternalSlots;var internalSlots=getInternalSlots(dtf);/** IMPL END */var pattern=internalSlots.pattern;return (0, FormatDateTimePattern_1.FormatDateTimePattern)(dtf,(0, lib.PartitionPattern)(pattern),x,implDetails);}exports.PartitionDateTimePattern=PartitionDateTimePattern;});unwrapExports(PartitionDateTimePattern_1);PartitionDateTimePattern_1.PartitionDateTimePattern;

var FormatDateTime_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.FormatDateTime=void 0;/**
 * https://tc39.es/ecma402/#sec-formatdatetime
 * @param dtf DateTimeFormat
 * @param x
 */function FormatDateTime(dtf,x,implDetails){var parts=(0, PartitionDateTimePattern_1.PartitionDateTimePattern)(dtf,x,implDetails);var result='';for(var _i=0,parts_1=parts;_i<parts_1.length;_i++){var part=parts_1[_i];result+=part.value;}return result;}exports.FormatDateTime=FormatDateTime;});unwrapExports(FormatDateTime_1);FormatDateTime_1.FormatDateTime;

var BasicFormatMatcher_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.BasicFormatMatcher=void 0;/**
 * https://tc39.es/ecma402/#sec-basicformatmatcher
 * @param options
 * @param formats
 */function BasicFormatMatcher(options,formats){var bestScore=-Infinity;var bestFormat=formats[0];(0, lib.invariant)(Array.isArray(formats),'formats should be a list of things');for(var _i=0,formats_1=formats;_i<formats_1.length;_i++){var format=formats_1[_i];var score=0;for(var _a=0,DATE_TIME_PROPS_1=utils.DATE_TIME_PROPS;_a<DATE_TIME_PROPS_1.length;_a++){var prop=DATE_TIME_PROPS_1[_a];var optionsProp=options[prop];var formatProp=format[prop];if(optionsProp===undefined&&formatProp!==undefined){score-=utils.additionPenalty;}else if(optionsProp!==undefined&&formatProp===undefined){score-=utils.removalPenalty;}else if(optionsProp!==formatProp){var values=void 0;if(prop==='fractionalSecondDigits'){values=[1,2,3];}else {values=['2-digit','numeric','narrow','short','long'];}var optionsPropIndex=values.indexOf(optionsProp);var formatPropIndex=values.indexOf(formatProp);var delta=Math.max(-2,Math.min(formatPropIndex-optionsPropIndex,2));if(delta===2){score-=utils.longMorePenalty;}else if(delta===1){score-=utils.shortMorePenalty;}else if(delta===-1){score-=utils.shortLessPenalty;}else if(delta===-2){score-=utils.longLessPenalty;}}}if(score>bestScore){bestScore=score;bestFormat=format;}}return (0, tslib_es6.__assign)({},bestFormat);}exports.BasicFormatMatcher=BasicFormatMatcher;});unwrapExports(BasicFormatMatcher_1);BasicFormatMatcher_1.BasicFormatMatcher;

var skeleton=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.splitRangePattern=exports.splitFallbackRangePattern=exports.parseDateTimeSkeleton=exports.processDateTimePattern=void 0;/**
 * https://unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
 * Credit: https://github.com/caridy/intl-datetimeformat-pattern/blob/master/index.js
 * with some tweaks
 */var DATE_TIME_REGEX=/(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;// trim patterns after transformations
var expPatternTrimmer=/^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g;function matchSkeletonPattern(match,result){var len=match.length;switch(match[0]){// Era
case'G':result.era=len===4?'long':len===5?'narrow':'short';return '{era}';// Year
case'y':case'Y':case'u':case'U':case'r':result.year=len===2?'2-digit':'numeric';return '{year}';// Quarter
case'q':case'Q':throw new RangeError('`w/Q` (quarter) patterns are not supported');// Month
case'M':case'L':result.month=['numeric','2-digit','short','long','narrow'][len-1];return '{month}';// Week
case'w':case'W':throw new RangeError('`w/W` (week of year) patterns are not supported');case'd':result.day=['numeric','2-digit'][len-1];return '{day}';case'D':case'F':case'g':result.day='numeric';return '{day}';// Weekday
case'E':result.weekday=len===4?'long':len===5?'narrow':'short';return '{weekday}';case'e':result.weekday=[undefined,undefined,'short','long','narrow','short'][len-1];return '{weekday}';case'c':result.weekday=[undefined,undefined,'short','long','narrow','short'][len-1];return '{weekday}';// Period
case'a':// AM, PM
case'b':// am, pm, noon, midnight
case'B':// flexible day periods
result.hour12=true;return '{ampm}';// Hour
case'h':result.hour=['numeric','2-digit'][len-1];result.hour12=true;return '{hour}';case'H':result.hour=['numeric','2-digit'][len-1];return '{hour}';case'K':result.hour=['numeric','2-digit'][len-1];result.hour12=true;return '{hour}';case'k':result.hour=['numeric','2-digit'][len-1];return '{hour}';case'j':case'J':case'C':throw new RangeError('`j/J/C` (hour) patterns are not supported, use `h/H/K/k` instead');// Minute
case'm':result.minute=['numeric','2-digit'][len-1];return '{minute}';// Second
case's':result.second=['numeric','2-digit'][len-1];return '{second}';case'S':case'A':result.second='numeric';return '{second}';// Zone
case'z':// 1..3, 4: specific non-location format
case'Z':// 1..3, 4, 5: The ISO8601 varios formats
case'O':// 1, 4: miliseconds in day short, long
case'v':// 1, 4: generic non-location format
case'V':// 1, 2, 3, 4: time zone ID or city
case'X':// 1, 2, 3, 4: The ISO8601 varios formats
case'x':// 1, 2, 3, 4: The ISO8601 varios formats
result.timeZoneName=len<4?'short':'long';return '{timeZoneName}';}return '';}function skeletonTokenToTable2(c){switch(c){// Era
case'G':return 'era';// Year
case'y':case'Y':case'u':case'U':case'r':return 'year';// Month
case'M':case'L':return 'month';// Day
case'd':case'D':case'F':case'g':return 'day';// Period
case'a':// AM, PM
case'b':// am, pm, noon, midnight
case'B':// flexible day periods
return 'ampm';// Hour
case'h':case'H':case'K':case'k':return 'hour';// Minute
case'm':return 'minute';// Second
case's':case'S':case'A':return 'second';default:throw new RangeError('Invalid range pattern token');}}function processDateTimePattern(pattern,result){var literals=[];// Use skeleton to populate result, but use mapped pattern to populate pattern
var pattern12=pattern// Double apostrophe
.replace(/'{2}/g,'{apostrophe}')// Apostrophe-escaped
.replace(/'(.*?)'/g,function(_,literal){literals.push(literal);return "$$".concat(literals.length-1,"$$");}).replace(DATE_TIME_REGEX,function(m){return matchSkeletonPattern(m,result||{});});//Restore literals
if(literals.length){pattern12=pattern12.replace(/\$\$(\d+)\$\$/g,function(_,i){return literals[+i];}).replace(/\{apostrophe\}/g,"'");}// Handle apostrophe-escaped things
return [pattern12.replace(/([\s\uFEFF\xA0])\{ampm\}([\s\uFEFF\xA0])/,'$1').replace('{ampm}','').replace(expPatternTrimmer,''),pattern12];}exports.processDateTimePattern=processDateTimePattern;/**
 * Parse Date time skeleton into Intl.DateTimeFormatOptions
 * Ref: https://unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table
 * @public
 * @param skeleton skeleton string
 */function parseDateTimeSkeleton(skeleton,rawPattern,rangePatterns,intervalFormatFallback){if(rawPattern===void 0){rawPattern=skeleton;}var result={pattern:'',pattern12:'',skeleton:skeleton,rawPattern:rawPattern,rangePatterns:{},rangePatterns12:{}};if(rangePatterns){for(var k in rangePatterns){var key=skeletonTokenToTable2(k);var rawPattern_1=rangePatterns[k];var intervalResult={patternParts:[]};var _a=processDateTimePattern(rawPattern_1,intervalResult),pattern_1=_a[0],pattern12_1=_a[1];result.rangePatterns[key]=(0, tslib_es6.__assign)((0, tslib_es6.__assign)({},intervalResult),{patternParts:splitRangePattern(pattern_1)});result.rangePatterns12[key]=(0, tslib_es6.__assign)((0, tslib_es6.__assign)({},intervalResult),{patternParts:splitRangePattern(pattern12_1)});}}if(intervalFormatFallback){var patternParts=splitFallbackRangePattern(intervalFormatFallback);result.rangePatterns.default={patternParts:patternParts};result.rangePatterns12.default={patternParts:patternParts};}// Process skeleton
skeleton.replace(DATE_TIME_REGEX,function(m){return matchSkeletonPattern(m,result);});var _b=processDateTimePattern(rawPattern),pattern=_b[0],pattern12=_b[1];result.pattern=pattern;result.pattern12=pattern12;return result;}exports.parseDateTimeSkeleton=parseDateTimeSkeleton;function splitFallbackRangePattern(pattern){var parts=pattern.split(/(\{[0|1]\})/g).filter(Boolean);return parts.map(function(pattern){switch(pattern){case'{0}':return {source:lib.RangePatternType.startRange,pattern:pattern};case'{1}':return {source:lib.RangePatternType.endRange,pattern:pattern};default:return {source:lib.RangePatternType.shared,pattern:pattern};}});}exports.splitFallbackRangePattern=splitFallbackRangePattern;function splitRangePattern(pattern){var PART_REGEX=/\{(.*?)\}/g;// Map of part and index within the string
var parts={};var match;var splitIndex=0;while(match=PART_REGEX.exec(pattern)){if(!(match[0]in parts)){parts[match[0]]=match.index;}else {splitIndex=match.index;break;}}if(!splitIndex){return [{source:lib.RangePatternType.startRange,pattern:pattern}];}return [{source:lib.RangePatternType.startRange,pattern:pattern.slice(0,splitIndex)},{source:lib.RangePatternType.endRange,pattern:pattern.slice(splitIndex)}];}exports.splitRangePattern=splitRangePattern;});unwrapExports(skeleton);skeleton.splitRangePattern;skeleton.splitFallbackRangePattern;skeleton.parseDateTimeSkeleton;skeleton.processDateTimePattern;

var BestFitFormatMatcher_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.BestFitFormatMatcher=exports.bestFitFormatMatcherScore=void 0;function isNumericType(t){return t==='numeric'||t==='2-digit';}/**
 * Credit: https://github.com/andyearnshaw/Intl.js/blob/0958dc1ad8153f1056653ea22b8208f0df289a4e/src/12.datetimeformat.js#L611
 * with some modifications
 * @param options
 * @param format
 */function bestFitFormatMatcherScore(options,format){var score=0;if(options.hour12&&!format.hour12){score-=utils.removalPenalty;}else if(!options.hour12&&format.hour12){score-=utils.additionPenalty;}for(var _i=0,DATE_TIME_PROPS_1=utils.DATE_TIME_PROPS;_i<DATE_TIME_PROPS_1.length;_i++){var prop=DATE_TIME_PROPS_1[_i];var optionsProp=options[prop];var formatProp=format[prop];if(optionsProp===undefined&&formatProp!==undefined){score-=utils.additionPenalty;}else if(optionsProp!==undefined&&formatProp===undefined){score-=utils.removalPenalty;}else if(optionsProp!==formatProp){// extra penalty for numeric vs non-numeric
if(isNumericType(optionsProp)!==isNumericType(formatProp)){score-=utils.differentNumericTypePenalty;}else {var values=['2-digit','numeric','narrow','short','long'];var optionsPropIndex=values.indexOf(optionsProp);var formatPropIndex=values.indexOf(formatProp);var delta=Math.max(-2,Math.min(formatPropIndex-optionsPropIndex,2));if(delta===2){score-=utils.longMorePenalty;}else if(delta===1){score-=utils.shortMorePenalty;}else if(delta===-1){score-=utils.shortLessPenalty;}else if(delta===-2){score-=utils.longLessPenalty;}}}}return score;}exports.bestFitFormatMatcherScore=bestFitFormatMatcherScore;/**
 * https://tc39.es/ecma402/#sec-bestfitformatmatcher
 * Just alias to basic for now
 * @param options
 * @param formats
 * @param implDetails Implementation details
 */function BestFitFormatMatcher(options,formats){var bestScore=-Infinity;var bestFormat=formats[0];(0, lib.invariant)(Array.isArray(formats),'formats should be a list of things');for(var _i=0,formats_1=formats;_i<formats_1.length;_i++){var format=formats_1[_i];var score=bestFitFormatMatcherScore(options,format);if(score>bestScore){bestScore=score;bestFormat=format;}}var skeletonFormat=(0, tslib_es6.__assign)({},bestFormat);var patternFormat={rawPattern:bestFormat.rawPattern};(0, skeleton.processDateTimePattern)(bestFormat.rawPattern,patternFormat);// Kinda following https://github.com/unicode-org/icu/blob/dd50e38f459d84e9bf1b0c618be8483d318458ad/icu4j/main/classes/core/src/com/ibm/icu/text/DateTimePatternGenerator.java
// Method adjustFieldTypes
for(var prop in skeletonFormat){var skeletonValue=skeletonFormat[prop];var patternValue=patternFormat[prop];var requestedValue=options[prop];// Don't mess with minute/second or we can get in the situation of
// 7:0:0 which is weird
if(prop==='minute'||prop==='second'){continue;}// Nothing to do here
if(!requestedValue){continue;}// https://unicode.org/reports/tr35/tr35-dates.html#Matching_Skeletons
// Looks like we should not convert numeric to alphabetic but the other way
// around is ok
if(isNumericType(patternValue)&&!isNumericType(requestedValue)){continue;}if(skeletonValue===requestedValue){continue;}patternFormat[prop]=requestedValue;}// Copy those over
patternFormat.pattern=skeletonFormat.pattern;patternFormat.pattern12=skeletonFormat.pattern12;patternFormat.skeleton=skeletonFormat.skeleton;patternFormat.rangePatterns=skeletonFormat.rangePatterns;patternFormat.rangePatterns12=skeletonFormat.rangePatterns12;return patternFormat;}exports.BestFitFormatMatcher=BestFitFormatMatcher;});unwrapExports(BestFitFormatMatcher_1);BestFitFormatMatcher_1.BestFitFormatMatcher;BestFitFormatMatcher_1.bestFitFormatMatcherScore;

var DateTimeStyleFormat_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.DateTimeStyleFormat=void 0;function DateTimeStyleFormat(dateStyle,timeStyle,dataLocaleData){var dateFormat,timeFormat;if(timeStyle!==undefined){(0, lib.invariant)(timeStyle==='full'||timeStyle==='long'||timeStyle==='medium'||timeStyle==='short','invalid timeStyle');timeFormat=dataLocaleData.timeFormat[timeStyle];}if(dateStyle!==undefined){(0, lib.invariant)(dateStyle==='full'||dateStyle==='long'||dateStyle==='medium'||dateStyle==='short','invalid dateStyle');dateFormat=dataLocaleData.dateFormat[dateStyle];}if(dateStyle!==undefined&&timeStyle!==undefined){var format={};for(var field in dateFormat){if(field!=='pattern'){// @ts-ignore
format[field]=dateFormat[field];}}for(var field in timeFormat){if(field!=='pattern'&&field!=='pattern12'){// @ts-ignore
format[field]=timeFormat[field];}}var connector=dataLocaleData.dateTimeFormat[dateStyle];var pattern=connector.replace('{0}',timeFormat.pattern).replace('{1}',dateFormat.pattern);format.pattern=pattern;if('pattern12'in timeFormat){var pattern12=connector.replace('{0}',timeFormat.pattern12).replace('{1}',dateFormat.pattern);format.pattern12=pattern12;}return format;}if(timeStyle!==undefined){return timeFormat;}(0, lib.invariant)(dateStyle!==undefined,'dateStyle should not be undefined');return dateFormat;}exports.DateTimeStyleFormat=DateTimeStyleFormat;});unwrapExports(DateTimeStyleFormat_1);DateTimeStyleFormat_1.DateTimeStyleFormat;

var ToDateTimeOptions_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.ToDateTimeOptions=void 0;/**
 * https://tc39.es/ecma402/#sec-todatetimeoptions
 * @param options
 * @param required
 * @param defaults
 */function ToDateTimeOptions(options,required,defaults){if(options===undefined){options=null;}else {options=(0, lib.ToObject)(options);}options=Object.create(options);var needDefaults=true;if(required==='date'||required==='any'){for(var _i=0,_a=['weekday','year','month','day'];_i<_a.length;_i++){var prop=_a[_i];var value=options[prop];if(value!==undefined){needDefaults=false;}}}if(required==='time'||required==='any'){for(var _b=0,_c=['dayPeriod','hour','minute','second','fractionalSecondDigits'];_b<_c.length;_b++){var prop=_c[_b];var value=options[prop];if(value!==undefined){needDefaults=false;}}}if(options.dateStyle!==undefined||options.timeStyle!==undefined){needDefaults=false;}if(required==='date'&&options.timeStyle){throw new TypeError('Intl.DateTimeFormat date was required but timeStyle was included');}if(required==='time'&&options.dateStyle){throw new TypeError('Intl.DateTimeFormat time was required but dateStyle was included');}if(needDefaults&&(defaults==='date'||defaults==='all')){for(var _d=0,_e=['year','month','day'];_d<_e.length;_d++){var prop=_e[_d];options[prop]='numeric';}}if(needDefaults&&(defaults==='time'||defaults==='all')){for(var _f=0,_g=['hour','minute','second'];_f<_g.length;_f++){var prop=_g[_f];options[prop]='numeric';}}return options;}exports.ToDateTimeOptions=ToDateTimeOptions;});unwrapExports(ToDateTimeOptions_1);ToDateTimeOptions_1.ToDateTimeOptions;

var InitializeDateTimeFormat_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.InitializeDateTimeFormat=void 0;function isTimeRelated(opt){for(var _i=0,_a=['hour','minute','second'];_i<_a.length;_i++){var prop=_a[_i];var value=opt[prop];if(value!==undefined){return true;}}return false;}function resolveHourCycle(hc,hcDefault,hour12){if(hc==null){hc=hcDefault;}if(hour12!==undefined){if(hour12){if(hcDefault==='h11'||hcDefault==='h23'){hc='h11';}else {hc='h12';}}else {(0, lib.invariant)(!hour12,'hour12 must not be set');if(hcDefault==='h11'||hcDefault==='h23'){hc='h23';}else {hc='h24';}}}return hc;}var TYPE_REGEX=/^[a-z0-9]{3,8}$/i;/**
 * https://tc39.es/ecma402/#sec-initializedatetimeformat
 * @param dtf DateTimeFormat
 * @param locales locales
 * @param opts options
 */function InitializeDateTimeFormat(dtf,locales,opts,_a){var getInternalSlots=_a.getInternalSlots,availableLocales=_a.availableLocales,localeData=_a.localeData,getDefaultLocale=_a.getDefaultLocale,getDefaultTimeZone=_a.getDefaultTimeZone,relevantExtensionKeys=_a.relevantExtensionKeys,tzData=_a.tzData,uppercaseLinks=_a.uppercaseLinks;// @ts-ignore
var requestedLocales=(0, lib.CanonicalizeLocaleList)(locales);var options=(0, ToDateTimeOptions_1.ToDateTimeOptions)(opts,'any','date');var opt=Object.create(null);var matcher=(0, lib.GetOption)(options,'localeMatcher','string',['lookup','best fit'],'best fit');opt.localeMatcher=matcher;var calendar=(0, lib.GetOption)(options,'calendar','string',undefined,undefined);if(calendar!==undefined&&!TYPE_REGEX.test(calendar)){throw new RangeError('Malformed calendar');}var internalSlots=getInternalSlots(dtf);opt.ca=calendar;var numberingSystem=(0, lib.GetOption)(options,'numberingSystem','string',undefined,undefined);if(numberingSystem!==undefined&&!TYPE_REGEX.test(numberingSystem)){throw new RangeError('Malformed numbering system');}opt.nu=numberingSystem;var hour12=(0, lib.GetOption)(options,'hour12','boolean',undefined,undefined);var hourCycle=(0, lib.GetOption)(options,'hourCycle','string',['h11','h12','h23','h24'],undefined);if(hour12!==undefined){// @ts-ignore
hourCycle=null;}opt.hc=hourCycle;var r=(0, intlLocalematcher.ResolveLocale)(availableLocales,requestedLocales,opt,relevantExtensionKeys,localeData,getDefaultLocale);internalSlots.locale=r.locale;calendar=r.ca;internalSlots.calendar=calendar;internalSlots.hourCycle=r.hc;internalSlots.numberingSystem=r.nu;var dataLocale=r.dataLocale;internalSlots.dataLocale=dataLocale;var timeZone=options.timeZone;if(timeZone!==undefined){timeZone=String(timeZone);if(!(0, lib.IsValidTimeZoneName)(timeZone,{tzData:tzData,uppercaseLinks:uppercaseLinks})){throw new RangeError('Invalid timeZoneName');}timeZone=(0, lib.CanonicalizeTimeZoneName)(timeZone,{tzData:tzData,uppercaseLinks:uppercaseLinks});}else {timeZone=getDefaultTimeZone();}internalSlots.timeZone=timeZone;opt=Object.create(null);opt.weekday=(0, lib.GetOption)(options,'weekday','string',['narrow','short','long'],undefined);opt.era=(0, lib.GetOption)(options,'era','string',['narrow','short','long'],undefined);opt.year=(0, lib.GetOption)(options,'year','string',['2-digit','numeric'],undefined);opt.month=(0, lib.GetOption)(options,'month','string',['2-digit','numeric','narrow','short','long'],undefined);opt.day=(0, lib.GetOption)(options,'day','string',['2-digit','numeric'],undefined);opt.hour=(0, lib.GetOption)(options,'hour','string',['2-digit','numeric'],undefined);opt.minute=(0, lib.GetOption)(options,'minute','string',['2-digit','numeric'],undefined);opt.second=(0, lib.GetOption)(options,'second','string',['2-digit','numeric'],undefined);opt.timeZoneName=(0, lib.GetOption)(options,'timeZoneName','string',['short','long'],undefined);opt.fractionalSecondDigits=(0, lib.GetNumberOption)(options,'fractionalSecondDigits',1,3,// @ts-expect-error
undefined);var dataLocaleData=localeData[dataLocale];(0, lib.invariant)(!!dataLocaleData,"Missing locale data for ".concat(dataLocale));var formats=dataLocaleData.formats[calendar];// UNSPECCED: IMPLEMENTATION DETAILS
if(!formats){throw new RangeError("Calendar \"".concat(calendar,"\" is not supported. Try setting \"calendar\" to 1 of the following: ").concat(Object.keys(dataLocaleData.formats).join(', ')));}var formatMatcher=(0, lib.GetOption)(options,'formatMatcher','string',['basic','best fit'],'best fit');var dateStyle=(0, lib.GetOption)(options,'dateStyle','string',['full','long','medium','short'],undefined);internalSlots.dateStyle=dateStyle;var timeStyle=(0, lib.GetOption)(options,'timeStyle','string',['full','long','medium','short'],undefined);internalSlots.timeStyle=timeStyle;var bestFormat;if(dateStyle===undefined&&timeStyle===undefined){if(formatMatcher==='basic'){bestFormat=(0, BasicFormatMatcher_1.BasicFormatMatcher)(opt,formats);}else {// IMPL DETAILS START
if(isTimeRelated(opt)){var hc=resolveHourCycle(internalSlots.hourCycle,dataLocaleData.hourCycle,hour12);opt.hour12=hc==='h11'||hc==='h12';}// IMPL DETAILS END
bestFormat=(0, BestFitFormatMatcher_1.BestFitFormatMatcher)(opt,formats);}}else {for(var _i=0,DATE_TIME_PROPS_1=utils.DATE_TIME_PROPS;_i<DATE_TIME_PROPS_1.length;_i++){var prop=DATE_TIME_PROPS_1[_i];var p=opt[prop];if(p!==undefined){throw new TypeError("Intl.DateTimeFormat can't set option ".concat(prop," when ").concat(dateStyle?'dateStyle':'timeStyle'," is used"));}}bestFormat=(0, DateTimeStyleFormat_1.DateTimeStyleFormat)(dateStyle,timeStyle,dataLocaleData);}// IMPL DETAIL START
// For debugging
internalSlots.format=bestFormat;// IMPL DETAIL END
for(var prop in opt){var p=bestFormat[prop];if(p!==undefined){internalSlots[prop]=p;}}var pattern;var rangePatterns;if(internalSlots.hour!==undefined){var hc=resolveHourCycle(internalSlots.hourCycle,dataLocaleData.hourCycle,hour12);internalSlots.hourCycle=hc;if(hc==='h11'||hc==='h12'){pattern=bestFormat.pattern12;rangePatterns=bestFormat.rangePatterns12;}else {pattern=bestFormat.pattern;rangePatterns=bestFormat.rangePatterns;}}else {// @ts-ignore
internalSlots.hourCycle=undefined;pattern=bestFormat.pattern;rangePatterns=bestFormat.rangePatterns;}internalSlots.pattern=pattern;internalSlots.rangePatterns=rangePatterns;return dtf;}exports.InitializeDateTimeFormat=InitializeDateTimeFormat;});unwrapExports(InitializeDateTimeFormat_1);InitializeDateTimeFormat_1.InitializeDateTimeFormat;

var FormatDateTimeToParts_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.FormatDateTimeToParts=void 0;/**
 * https://tc39.es/ecma402/#sec-formatdatetimetoparts
 *
 * @param dtf
 * @param x
 * @param implDetails
 */function FormatDateTimeToParts(dtf,x,implDetails){var parts=(0, PartitionDateTimePattern_1.PartitionDateTimePattern)(dtf,x,implDetails);var result=(0, lib.ArrayCreate)(0);for(var _i=0,parts_1=parts;_i<parts_1.length;_i++){var part=parts_1[_i];result.push({type:part.type,value:part.value});}return result;}exports.FormatDateTimeToParts=FormatDateTimeToParts;});unwrapExports(FormatDateTimeToParts_1);FormatDateTimeToParts_1.FormatDateTimeToParts;

var PartitionDateTimeRangePattern_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.PartitionDateTimeRangePattern=void 0;var TABLE_2_FIELDS=['era','year','month','day','dayPeriod','ampm','hour','minute','second','fractionalSecondDigits'];function PartitionDateTimeRangePattern(dtf,x,y,implDetails){x=(0, lib.TimeClip)(x);if(isNaN(x)){throw new RangeError('Invalid start time');}y=(0, lib.TimeClip)(y);if(isNaN(y)){throw new RangeError('Invalid end time');}/** IMPL START */var getInternalSlots=implDetails.getInternalSlots,tzData=implDetails.tzData;var internalSlots=getInternalSlots(dtf);/** IMPL END */var tm1=(0, ToLocalTime_1.ToLocalTime)(x,// @ts-ignore
internalSlots.calendar,internalSlots.timeZone,{tzData:tzData});var tm2=(0, ToLocalTime_1.ToLocalTime)(y,// @ts-ignore
internalSlots.calendar,internalSlots.timeZone,{tzData:tzData});var pattern=internalSlots.pattern,rangePatterns=internalSlots.rangePatterns;var rangePattern;var dateFieldsPracticallyEqual=true;var patternContainsLargerDateField=false;for(var _i=0,TABLE_2_FIELDS_1=TABLE_2_FIELDS;_i<TABLE_2_FIELDS_1.length;_i++){var fieldName=TABLE_2_FIELDS_1[_i];if(dateFieldsPracticallyEqual&&!patternContainsLargerDateField){var rp=fieldName in rangePatterns?rangePatterns[fieldName]:undefined;if(rangePattern!==undefined&&rp===undefined){patternContainsLargerDateField=true;}else {rangePattern=rp;if(fieldName==='ampm'){var v1=tm1.hour;var v2=tm2.hour;if(v1>11&&v2<11||v1<11&&v2>11){dateFieldsPracticallyEqual=false;}}else if(fieldName==='dayPeriod');else if(fieldName==='fractionalSecondDigits'){var fractionalSecondDigits=internalSlots.fractionalSecondDigits;if(fractionalSecondDigits===undefined){fractionalSecondDigits=3;}var v1=Math.floor(tm1.millisecond*Math.pow(10,fractionalSecondDigits-3));var v2=Math.floor(tm2.millisecond*Math.pow(10,fractionalSecondDigits-3));if(!(0, lib.SameValue)(v1,v2)){dateFieldsPracticallyEqual=false;}}else {var v1=tm1[fieldName];var v2=tm2[fieldName];if(!(0, lib.SameValue)(v1,v2)){dateFieldsPracticallyEqual=false;}}}}}if(dateFieldsPracticallyEqual){var result_2=(0, FormatDateTimePattern_1.FormatDateTimePattern)(dtf,(0, lib.PartitionPattern)(pattern),x,implDetails);for(var _a=0,result_1=result_2;_a<result_1.length;_a++){var r=result_1[_a];r.source=lib.RangePatternType.shared;}return result_2;}var result=[];if(rangePattern===undefined){rangePattern=rangePatterns.default;/** IMPL DETAILS */ // Now we have to replace {0} & {1} with actual pattern
for(var _b=0,_c=rangePattern.patternParts;_b<_c.length;_b++){var patternPart=_c[_b];if(patternPart.pattern==='{0}'||patternPart.pattern==='{1}'){patternPart.pattern=pattern;}}}for(var _d=0,_e=rangePattern.patternParts;_d<_e.length;_d++){var rangePatternPart=_e[_d];var source=rangePatternPart.source,pattern_1=rangePatternPart.pattern;var z=void 0;if(source===lib.RangePatternType.startRange||source===lib.RangePatternType.shared){z=x;}else {z=y;}var patternParts=(0, lib.PartitionPattern)(pattern_1);var partResult=(0, FormatDateTimePattern_1.FormatDateTimePattern)(dtf,patternParts,z,implDetails);for(var _f=0,partResult_1=partResult;_f<partResult_1.length;_f++){var r=partResult_1[_f];r.source=source;}result=result.concat(partResult);}return result;}exports.PartitionDateTimeRangePattern=PartitionDateTimeRangePattern;});unwrapExports(PartitionDateTimeRangePattern_1);PartitionDateTimeRangePattern_1.PartitionDateTimeRangePattern;

var FormatDateTimeRangeToParts_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.FormatDateTimeRangeToParts=void 0;function FormatDateTimeRangeToParts(dtf,x,y,implDetails){var parts=(0, PartitionDateTimeRangePattern_1.PartitionDateTimeRangePattern)(dtf,x,y,implDetails);var result=new Array(0);for(var _i=0,parts_1=parts;_i<parts_1.length;_i++){var part=parts_1[_i];result.push({type:part.type,value:part.value,source:part.source});}return result;}exports.FormatDateTimeRangeToParts=FormatDateTimeRangeToParts;});unwrapExports(FormatDateTimeRangeToParts_1);FormatDateTimeRangeToParts_1.FormatDateTimeRangeToParts;

var FormatDateTimeRange_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.FormatDateTimeRange=void 0;function FormatDateTimeRange(dtf,x,y,implDetails){var parts=(0, PartitionDateTimeRangePattern_1.PartitionDateTimeRangePattern)(dtf,x,y,implDetails);var result='';for(var _i=0,parts_1=parts;_i<parts_1.length;_i++){var part=parts_1[_i];result+=part.value;}return result;}exports.FormatDateTimeRange=FormatDateTimeRange;});unwrapExports(FormatDateTimeRange_1);FormatDateTimeRange_1.FormatDateTimeRange;

var core=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.DateTimeFormat=void 0;var get_internal_slots_1=(0, tslib_es6.__importDefault)(get_internal_slots);var links_1=(0, tslib_es6.__importDefault)(links);var UPPERCASED_LINKS=Object.keys(links_1.default).reduce(function(all,l){all[l.toUpperCase()]=links_1.default[l];return all;},{});var RESOLVED_OPTIONS_KEYS=['locale','calendar','numberingSystem','dateStyle','timeStyle','timeZone','hourCycle','weekday','era','year','month','day','hour','minute','second','timeZoneName'];var formatDescriptor={enumerable:false,configurable:true,get:function(){if(typeof this!=='object'||!(0, lib.OrdinaryHasInstance)(exports.DateTimeFormat,this)){throw TypeError('Intl.DateTimeFormat format property accessor called on incompatible receiver');}var internalSlots=(0, get_internal_slots_1.default)(this);// eslint-disable-next-line @typescript-eslint/no-this-alias
var dtf=this;var boundFormat=internalSlots.boundFormat;if(boundFormat===undefined){// https://tc39.es/proposal-unified-intl-numberformat/section11/numberformat_diff_out.html#sec-number-format-functions
boundFormat=function(date){var x;if(date===undefined){x=Date.now();}else {x=Number(date);}return (0, FormatDateTime_1.FormatDateTime)(dtf,x,{getInternalSlots:get_internal_slots_1.default,localeData:exports.DateTimeFormat.localeData,tzData:exports.DateTimeFormat.tzData,getDefaultTimeZone:exports.DateTimeFormat.getDefaultTimeZone});};try{// https://github.com/tc39/test262/blob/master/test/intl402/NumberFormat/prototype/format/format-function-name.js
Object.defineProperty(boundFormat,'name',{configurable:true,enumerable:false,writable:false,value:''});}catch(e){// In older browser (e.g Chrome 36 like polyfill.io)
// TypeError: Cannot redefine property: name
}internalSlots.boundFormat=boundFormat;}return boundFormat;}};try{// https://github.com/tc39/test262/blob/master/test/intl402/NumberFormat/prototype/format/name.js
Object.defineProperty(formatDescriptor.get,'name',{configurable:true,enumerable:false,writable:false,value:'get format'});}catch(e){// In older browser (e.g Chrome 36 like polyfill.io)
// TypeError: Cannot redefine property: name
}exports.DateTimeFormat=function(locales,options){// Cannot use `new.target` bc of IE11 & TS transpiles it to something else
if(!this||!(0, lib.OrdinaryHasInstance)(exports.DateTimeFormat,this)){return new exports.DateTimeFormat(locales,options);}(0, InitializeDateTimeFormat_1.InitializeDateTimeFormat)(this,locales,options,{tzData:exports.DateTimeFormat.tzData,uppercaseLinks:UPPERCASED_LINKS,availableLocales:exports.DateTimeFormat.availableLocales,relevantExtensionKeys:exports.DateTimeFormat.relevantExtensionKeys,getDefaultLocale:exports.DateTimeFormat.getDefaultLocale,getDefaultTimeZone:exports.DateTimeFormat.getDefaultTimeZone,getInternalSlots:get_internal_slots_1.default,localeData:exports.DateTimeFormat.localeData});/** IMPL START */var internalSlots=(0, get_internal_slots_1.default)(this);var dataLocale=internalSlots.dataLocale;var dataLocaleData=exports.DateTimeFormat.localeData[dataLocale];(0, lib.invariant)(dataLocaleData!==undefined,"Cannot load locale-dependent data for ".concat(dataLocale,"."));/** IMPL END */};// Static properties
(0, lib.defineProperty)(exports.DateTimeFormat,'supportedLocalesOf',{value:function supportedLocalesOf(locales,options){return (0, lib.SupportedLocales)(exports.DateTimeFormat.availableLocales,(0, lib.CanonicalizeLocaleList)(locales),options);}});(0, lib.defineProperty)(exports.DateTimeFormat.prototype,'resolvedOptions',{value:function resolvedOptions(){if(typeof this!=='object'||!(0, lib.OrdinaryHasInstance)(exports.DateTimeFormat,this)){throw TypeError('Method Intl.DateTimeFormat.prototype.resolvedOptions called on incompatible receiver');}var internalSlots=(0, get_internal_slots_1.default)(this);var ro={};for(var _i=0,RESOLVED_OPTIONS_KEYS_1=RESOLVED_OPTIONS_KEYS;_i<RESOLVED_OPTIONS_KEYS_1.length;_i++){var key=RESOLVED_OPTIONS_KEYS_1[_i];var value=internalSlots[key];if(key==='hourCycle'){var hour12=value==='h11'||value==='h12'?true:value==='h23'||value==='h24'?false:undefined;if(hour12!==undefined){ro.hour12=hour12;}}if(utils.DATE_TIME_PROPS.indexOf(key)>-1){if(internalSlots.dateStyle!==undefined||internalSlots.timeStyle!==undefined){value=undefined;}}if(value!==undefined){ro[key]=value;}}return ro;}});(0, lib.defineProperty)(exports.DateTimeFormat.prototype,'formatToParts',{value:function formatToParts(date){if(date===undefined){date=Date.now();}else {date=(0, lib.ToNumber)(date);}return (0, FormatDateTimeToParts_1.FormatDateTimeToParts)(this,date,{getInternalSlots:get_internal_slots_1.default,localeData:exports.DateTimeFormat.localeData,tzData:exports.DateTimeFormat.tzData,getDefaultTimeZone:exports.DateTimeFormat.getDefaultTimeZone});}});(0, lib.defineProperty)(exports.DateTimeFormat.prototype,'formatRangeToParts',{value:function formatRangeToParts(startDate,endDate){var dtf=this;if(typeof dtf!=='object'){throw new TypeError();}if(startDate===undefined||endDate===undefined){throw new TypeError('startDate/endDate cannot be undefined');}var x=(0, lib.ToNumber)(startDate);var y=(0, lib.ToNumber)(endDate);return (0, FormatDateTimeRangeToParts_1.FormatDateTimeRangeToParts)(dtf,x,y,{getInternalSlots:get_internal_slots_1.default,localeData:exports.DateTimeFormat.localeData,tzData:exports.DateTimeFormat.tzData,getDefaultTimeZone:exports.DateTimeFormat.getDefaultTimeZone});}});(0, lib.defineProperty)(exports.DateTimeFormat.prototype,'formatRange',{value:function formatRange(startDate,endDate){var dtf=this;if(typeof dtf!=='object'){throw new TypeError();}if(startDate===undefined||endDate===undefined){throw new TypeError('startDate/endDate cannot be undefined');}var x=(0, lib.ToNumber)(startDate);var y=(0, lib.ToNumber)(endDate);return (0, FormatDateTimeRange_1.FormatDateTimeRange)(dtf,x,y,{getInternalSlots:get_internal_slots_1.default,localeData:exports.DateTimeFormat.localeData,tzData:exports.DateTimeFormat.tzData,getDefaultTimeZone:exports.DateTimeFormat.getDefaultTimeZone});}});var DEFAULT_TIMEZONE='UTC';exports.DateTimeFormat.__setDefaultTimeZone=function(timeZone){if(timeZone!==undefined){timeZone=String(timeZone);if(!(0, lib.IsValidTimeZoneName)(timeZone,{tzData:exports.DateTimeFormat.tzData,uppercaseLinks:UPPERCASED_LINKS})){throw new RangeError('Invalid timeZoneName');}timeZone=(0, lib.CanonicalizeTimeZoneName)(timeZone,{tzData:exports.DateTimeFormat.tzData,uppercaseLinks:UPPERCASED_LINKS});}else {timeZone=DEFAULT_TIMEZONE;}exports.DateTimeFormat.__defaultTimeZone=timeZone;};exports.DateTimeFormat.relevantExtensionKeys=['nu','ca','hc'];exports.DateTimeFormat.__defaultTimeZone=DEFAULT_TIMEZONE;exports.DateTimeFormat.getDefaultTimeZone=function(){return exports.DateTimeFormat.__defaultTimeZone;};exports.DateTimeFormat.__addLocaleData=function __addLocaleData(){var data=[];for(var _i=0;_i<arguments.length;_i++){data[_i]=arguments[_i];}var _loop_1=function(d,locale){var dateFormat=d.dateFormat,timeFormat=d.timeFormat,dateTimeFormat=d.dateTimeFormat,formats=d.formats,intervalFormats=d.intervalFormats,rawData=(0, tslib_es6.__rest)(d,["dateFormat","timeFormat","dateTimeFormat","formats","intervalFormats"]);var processedData=(0, tslib_es6.__assign)((0, tslib_es6.__assign)({},rawData),{dateFormat:{full:(0, skeleton.parseDateTimeSkeleton)(dateFormat.full),long:(0, skeleton.parseDateTimeSkeleton)(dateFormat.long),medium:(0, skeleton.parseDateTimeSkeleton)(dateFormat.medium),short:(0, skeleton.parseDateTimeSkeleton)(dateFormat.short)},timeFormat:{full:(0, skeleton.parseDateTimeSkeleton)(timeFormat.full),long:(0, skeleton.parseDateTimeSkeleton)(timeFormat.long),medium:(0, skeleton.parseDateTimeSkeleton)(timeFormat.medium),short:(0, skeleton.parseDateTimeSkeleton)(timeFormat.short)},dateTimeFormat:{full:(0, skeleton.parseDateTimeSkeleton)(dateTimeFormat.full).pattern,long:(0, skeleton.parseDateTimeSkeleton)(dateTimeFormat.long).pattern,medium:(0, skeleton.parseDateTimeSkeleton)(dateTimeFormat.medium).pattern,short:(0, skeleton.parseDateTimeSkeleton)(dateTimeFormat.short).pattern},formats:{}});var _loop_2=function(calendar){processedData.formats[calendar]=Object.keys(formats[calendar]).map(function(skeleton$1){return (0, skeleton.parseDateTimeSkeleton)(skeleton$1,formats[calendar][skeleton$1],intervalFormats[skeleton$1],intervalFormats.intervalFormatFallback);});};for(var calendar in formats){_loop_2(calendar);}var minimizedLocale=new Intl.Locale(locale).minimize().toString();exports.DateTimeFormat.localeData[locale]=exports.DateTimeFormat.localeData[minimizedLocale]=processedData;exports.DateTimeFormat.availableLocales.add(locale);exports.DateTimeFormat.availableLocales.add(minimizedLocale);if(!exports.DateTimeFormat.__defaultLocale){exports.DateTimeFormat.__defaultLocale=minimizedLocale;}};for(var _a=0,data_1=data;_a<data_1.length;_a++){var _b=data_1[_a],d=_b.data,locale=_b.locale;_loop_1(d,locale);}};Object.defineProperty(exports.DateTimeFormat.prototype,'format',formatDescriptor);exports.DateTimeFormat.__defaultLocale='';exports.DateTimeFormat.localeData={};exports.DateTimeFormat.availableLocales=new Set();exports.DateTimeFormat.getDefaultLocale=function(){return exports.DateTimeFormat.__defaultLocale;};exports.DateTimeFormat.polyfilled=true;exports.DateTimeFormat.tzData={};exports.DateTimeFormat.__addTZData=function(d){exports.DateTimeFormat.tzData=(0, packer.unpack)(d);};try{if(typeof Symbol!=='undefined'){Object.defineProperty(exports.DateTimeFormat.prototype,Symbol.toStringTag,{value:'Intl.DateTimeFormat',writable:false,enumerable:false,configurable:true});}Object.defineProperty(exports.DateTimeFormat.prototype.constructor,'length',{value:1,writable:false,enumerable:false,configurable:true});}catch(e){// Meta fix so we're test262-compliant, not important
}});unwrapExports(core);core.DateTimeFormat;

var intlDatetimeformat=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});(0, tslib_es6.__exportStar)(core,exports);});unwrapExports(intlDatetimeformat);

var supportedLocales=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.supportedLocales=void 0;// This file is generated from supported-locales-gen.ts
exports.supportedLocales=["af-NA","af","agq","ak","am","ar-AE","ar-BH","ar-DJ","ar-DZ","ar-EG","ar-EH","ar-ER","ar-IL","ar-IQ","ar-JO","ar-KM","ar-KW","ar-LB","ar-LY","ar-MA","ar-MR","ar-OM","ar-PS","ar-QA","ar-SA","ar-SD","ar-SO","ar-SS","ar-SY","ar-TD","ar-TN","ar-YE","ar","as","asa","ast","az-Cyrl","az-Latn","az","bas","be-tarask","be","bem","bez","bg","bm","bn-IN","bn","bo-IN","bo","br","brx","bs-Cyrl","bs-Latn","bs","ca-AD","ca-ES-valencia","ca-FR","ca-IT","ca","ccp-IN","ccp","ce","ceb","cgg","chr","ckb-IR","ckb","cs","cy","da-GL","da","dav","de-AT","de-BE","de-CH","de-IT","de-LI","de-LU","de","dje","doi","dsb","dua","dyo","dz","ebu","ee-TG","ee","el-CY","el","en-001","en-150","en-AE","en-AG","en-AI","en-AS","en-AT","en-AU","en-BB","en-BE","en-BI","en-BM","en-BS","en-BW","en-BZ","en-CA","en-CC","en-CH","en-CK","en-CM","en-CX","en-CY","en-DE","en-DG","en-DK","en-DM","en-ER","en-FI","en-FJ","en-FK","en-FM","en-GB","en-GD","en-GG","en-GH","en-GI","en-GM","en-GU","en-GY","en-HK","en-IE","en-IL","en-IM","en-IN","en-IO","en-JE","en-JM","en-KE","en-KI","en-KN","en-KY","en-LC","en-LR","en-LS","en-MG","en-MH","en-MO","en-MP","en-MS","en-MT","en-MU","en-MW","en-MY","en-NA","en-NF","en-NG","en-NL","en-NR","en-NU","en-NZ","en-PG","en-PH","en-PK","en-PN","en-PR","en-PW","en-RW","en-SB","en-SC","en-SD","en-SE","en-SG","en-SH","en-SI","en-SL","en-SS","en-SX","en-SZ","en-TC","en-TK","en-TO","en-TT","en-TV","en-TZ","en-UG","en-UM","en-VC","en-VG","en-VI","en-VU","en-WS","en-ZA","en-ZM","en-ZW","en","eo","es-419","es-AR","es-BO","es-BR","es-BZ","es-CL","es-CO","es-CR","es-CU","es-DO","es-EA","es-EC","es-GQ","es-GT","es-HN","es-IC","es-MX","es-NI","es-PA","es-PE","es-PH","es-PR","es-PY","es-SV","es-US","es-UY","es-VE","es","et","eu","ewo","fa-AF","fa","ff-Adlm-BF","ff-Adlm-CM","ff-Adlm-GH","ff-Adlm-GM","ff-Adlm-GW","ff-Adlm-LR","ff-Adlm-MR","ff-Adlm-NE","ff-Adlm-NG","ff-Adlm-SL","ff-Adlm-SN","ff-Adlm","ff-Latn-BF","ff-Latn-CM","ff-Latn-GH","ff-Latn-GM","ff-Latn-GN","ff-Latn-GW","ff-Latn-LR","ff-Latn-MR","ff-Latn-NE","ff-Latn-NG","ff-Latn-SL","ff-Latn","ff","fi","fil","fo-DK","fo","fr-BE","fr-BF","fr-BI","fr-BJ","fr-BL","fr-CA","fr-CD","fr-CF","fr-CG","fr-CH","fr-CI","fr-CM","fr-DJ","fr-DZ","fr-GA","fr-GF","fr-GN","fr-GP","fr-GQ","fr-HT","fr-KM","fr-LU","fr-MA","fr-MC","fr-MF","fr-MG","fr-ML","fr-MQ","fr-MR","fr-MU","fr-NC","fr-NE","fr-PF","fr-PM","fr-RE","fr-RW","fr-SC","fr-SN","fr-SY","fr-TD","fr-TG","fr-TN","fr-VU","fr-WF","fr-YT","fr","fur","fy","ga-GB","ga","gd","gl","gsw-FR","gsw-LI","gsw","gu","guz","gv","ha-GH","ha-NE","ha","haw","he","hi","hr-BA","hr","hsb","hu","hy","ia","id","ig","ii","is","it-CH","it-SM","it-VA","it","ja","jgo","jmc","jv","ka","kab","kam","kde","kea","kgp","khq","ki","kk","kkj","kl","kln","km","kn","ko-KP","ko","kok","ks-Arab","ks","ksb","ksf","ksh","ku","kw","ky","lag","lb","lg","lkt","ln-AO","ln-CF","ln-CG","ln","lo","lrc-IQ","lrc","lt","lu","luo","luy","lv","mai","mas-TZ","mas","mer","mfe","mg","mgh","mgo","mi","mk","ml","mn","mni-Beng","mni","mr","ms-BN","ms-ID","ms-SG","ms","mt","mua","my","mzn","naq","nb-SJ","nb","nd","nds-NL","nds","ne-IN","ne","nl-AW","nl-BE","nl-BQ","nl-CW","nl-SR","nl-SX","nl","nmg","nn","nnh","no","nus","nyn","om-KE","om","or","os-RU","os","pa-Arab","pa-Guru","pa","pcm","pl","ps-PK","ps","pt-AO","pt-CH","pt-CV","pt-GQ","pt-GW","pt-LU","pt-MO","pt-MZ","pt-PT","pt-ST","pt-TL","pt","qu-BO","qu-EC","qu","rm","rn","ro-MD","ro","rof","ru-BY","ru-KG","ru-KZ","ru-MD","ru-UA","ru","rw","rwk","sa","sah","saq","sat-Olck","sat","sbp","sc","sd-Arab","sd-Deva","sd","se-FI","se-SE","se","seh","ses","sg","shi-Latn","shi-Tfng","shi","si","sk","sl","smn","sn","so-DJ","so-ET","so-KE","so","sq-MK","sq-XK","sq","sr-Cyrl-BA","sr-Cyrl-ME","sr-Cyrl-XK","sr-Cyrl","sr-Latn-BA","sr-Latn-ME","sr-Latn-XK","sr-Latn","sr","su-Latn","su","sv-AX","sv-FI","sv","sw-CD","sw-KE","sw-UG","sw","ta-LK","ta-MY","ta-SG","ta","te","teo-KE","teo","tg","th","ti-ER","ti","tk","to","tr-CY","tr","tt","twq","tzm","ug","uk","und","ur-IN","ur","uz-Arab","uz-Cyrl","uz-Latn","uz","vai-Latn","vai-Vaii","vai","vi","vun","wae","wo","xh","xog","yav","yi","yo-BJ","yo","yrl-CO","yrl-VE","yrl","yue-Hans","yue-Hant","yue","zgh","zh-Hans-HK","zh-Hans-MO","zh-Hans-SG","zh-Hans","zh-Hant-HK","zh-Hant-MO","zh-Hant","zh","zu"];});unwrapExports(supportedLocales);supportedLocales.supportedLocales;

var shouldPolyfill_1=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.shouldPolyfill=void 0;function supportsDateStyle(){try{return !!new Intl.DateTimeFormat(undefined,{dateStyle:'short'}).resolvedOptions().dateStyle;}catch(e){return false;}}/**
 * https://bugs.chromium.org/p/chromium/issues/detail?id=865351
 */function hasChromeLt71Bug(){try{return new Intl.DateTimeFormat('en',{hourCycle:'h11',hour:'numeric'}).formatToParts(0)[2].type!=='dayPeriod';}catch(e){return false;}}/**
 * Node 14's version of Intl.DateTimeFormat does not throw
 * when dateStyle/timeStyle is used with other options.
 * This was fixed in newer V8 versions
 */function hasUnthrownDateTimeStyleBug(){try{return !!new Intl.DateTimeFormat('en',{dateStyle:'short',hour:'numeric'}).format(new Date(0));}catch(e){return false;}}function supportedLocalesOf(locale){if(!locale){return true;}var locales=Array.isArray(locale)?locale:[locale];return Intl.DateTimeFormat.supportedLocalesOf(locales).length===locales.length;}function shouldPolyfill(locale){if(locale===void 0){locale='en';}if(!('DateTimeFormat'in Intl)||!('formatToParts'in Intl.DateTimeFormat.prototype)||!('formatRange'in Intl.DateTimeFormat.prototype)||hasChromeLt71Bug()||hasUnthrownDateTimeStyleBug()||!supportsDateStyle()||!supportedLocalesOf(locale)){return locale?(0, intlLocalematcher.match)([locale],supportedLocales.supportedLocales,'en'):undefined;}}exports.shouldPolyfill=shouldPolyfill;});unwrapExports(shouldPolyfill_1);shouldPolyfill_1.shouldPolyfill;

var to_locale_string=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});exports.toLocaleTimeString=exports.toLocaleDateString=exports.toLocaleString=void 0;// eslint-disable-next-line import/no-cycle
/**
 * Number.prototype.toLocaleString ponyfill
 * https://tc39.es/ecma402/#sup-number.prototype.tolocalestring
 */function toLocaleString(x,locales,options){var dtf=new core.DateTimeFormat(locales,options);return dtf.format(x);}exports.toLocaleString=toLocaleString;function toLocaleDateString(x,locales,options){var dtf=new core.DateTimeFormat(locales,(0, ToDateTimeOptions_1.ToDateTimeOptions)(options,'date','date'));return dtf.format(x);}exports.toLocaleDateString=toLocaleDateString;function toLocaleTimeString(x,locales,options){var dtf=new core.DateTimeFormat(locales,(0, ToDateTimeOptions_1.ToDateTimeOptions)(options,'time','time'));return dtf.format(x);}exports.toLocaleTimeString=toLocaleTimeString;});unwrapExports(to_locale_string);to_locale_string.toLocaleTimeString;to_locale_string.toLocaleDateString;

var polyfill=createCommonjsModule(function(module,exports){Object.defineProperty(exports,"__esModule",{value:true});if((0, shouldPolyfill_1.shouldPolyfill)()){(0, lib.defineProperty)(Intl,'DateTimeFormat',{value:intlDatetimeformat.DateTimeFormat});(0, lib.defineProperty)(Date.prototype,'toLocaleString',{value:function toLocaleString(locales,options){return (0, to_locale_string.toLocaleString)(this,locales,options);}});(0, lib.defineProperty)(Date.prototype,'toLocaleDateString',{value:function toLocaleDateString(locales,options){return (0, to_locale_string.toLocaleDateString)(this,locales,options);}});(0, lib.defineProperty)(Date.prototype,'toLocaleTimeString',{value:function toLocaleTimeString(locales,options){return (0, to_locale_string.toLocaleTimeString)(this,locales,options);}});}});var polyfill$1 = unwrapExports(polyfill);

export { polyfill as __moduleExports, polyfill$1 as default };
