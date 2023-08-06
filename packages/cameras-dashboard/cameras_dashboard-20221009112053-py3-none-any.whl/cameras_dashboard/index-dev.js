const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { U as __extends } from './main-dev.js';

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
*/function defineProperty(target,name,_a){var value=_a.value;Object.defineProperty(target,name,{configurable:true,enumerable:false,writable:true,value:value});}function invariant$1(condition,message,Err){if(Err===void 0){Err=Error;}if(!condition){throw new Err(message);}}

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

var UNICODE_EXTENSION_SEQUENCE_REGEX=/-u(?:-[0-9a-z]{2,8})+/gi;function invariant(condition,message,Err){if(Err===void 0){Err=Error;}if(!condition){throw new Err(message);}}

/**
 * https://tc39.es/ecma402/#sec-bestavailablelocale
 * @param availableLocales
 * @param locale
 */function BestAvailableLocale(availableLocales,locale){var candidate=locale;while(true){if(availableLocales.has(candidate)){return candidate;}var pos=candidate.lastIndexOf('-');if(!~pos){return undefined;}if(pos>=2&&candidate[pos-2]==='-'){pos-=2;}candidate=candidate.slice(0,pos);}}

/**
 * https://tc39.es/ecma402/#sec-lookupmatcher
 * @param availableLocales
 * @param requestedLocales
 * @param getDefaultLocale
 */function LookupMatcher(availableLocales,requestedLocales,getDefaultLocale){var result={locale:''};for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var locale=requestedLocales_1[_i];var noExtensionLocale=locale.replace(UNICODE_EXTENSION_SEQUENCE_REGEX,'');var availableLocale=BestAvailableLocale(availableLocales,noExtensionLocale);if(availableLocale){result.locale=availableLocale;if(locale!==noExtensionLocale){result.extension=locale.slice(noExtensionLocale.length+1,locale.length);}return result;}}result.locale=getDefaultLocale();return result;}

/**
 * https://tc39.es/ecma402/#sec-bestfitmatcher
 * @param availableLocales
 * @param requestedLocales
 * @param getDefaultLocale
 */function BestFitMatcher(availableLocales,requestedLocales,getDefaultLocale){var minimizedAvailableLocaleMap={};var availableLocaleMap={};var canonicalizedLocaleMap={};var minimizedAvailableLocales=new Set();availableLocales.forEach(function(locale){var minimizedLocale=new Intl.Locale(locale).minimize().toString();var canonicalizedLocale=Intl.getCanonicalLocales(locale)[0]||locale;minimizedAvailableLocaleMap[minimizedLocale]=locale;availableLocaleMap[locale]=locale;canonicalizedLocaleMap[canonicalizedLocale]=locale;minimizedAvailableLocales.add(minimizedLocale);minimizedAvailableLocales.add(locale);minimizedAvailableLocales.add(canonicalizedLocale);});var foundLocale;for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var l=requestedLocales_1[_i];if(foundLocale){break;}var noExtensionLocale=l.replace(UNICODE_EXTENSION_SEQUENCE_REGEX,'');if(availableLocales.has(noExtensionLocale)){foundLocale=noExtensionLocale;break;}if(minimizedAvailableLocales.has(noExtensionLocale)){foundLocale=noExtensionLocale;break;}var locale=new Intl.Locale(noExtensionLocale);var maximizedRequestedLocale=locale.maximize().toString();var minimizedRequestedLocale=locale.minimize().toString();// Check minimized locale
if(minimizedAvailableLocales.has(minimizedRequestedLocale)){foundLocale=minimizedRequestedLocale;break;}// Lookup algo on maximized locale
foundLocale=BestAvailableLocale(minimizedAvailableLocales,maximizedRequestedLocale);}if(!foundLocale){return {locale:getDefaultLocale()};}return {locale:availableLocaleMap[foundLocale]||canonicalizedLocaleMap[foundLocale]||minimizedAvailableLocaleMap[foundLocale]||foundLocale};}

/**
 * https://tc39.es/ecma402/#sec-unicodeextensionvalue
 * @param extension
 * @param key
 */function UnicodeExtensionValue(extension,key){invariant(key.length===2,'key must have 2 elements');var size=extension.length;var searchValue="-".concat(key,"-");var pos=extension.indexOf(searchValue);if(pos!==-1){var start=pos+4;var end=start;var k=start;var done=false;while(!done){var e=extension.indexOf('-',k);var len=void 0;if(e===-1){len=size-k;}else {len=e-k;}if(len===2){done=true;}else if(e===-1){end=size;done=true;}else {end=e;k=e+1;}}return extension.slice(start,end);}searchValue="-".concat(key);pos=extension.indexOf(searchValue);if(pos!==-1&&pos+3===size){return '';}return undefined;}

/**
 * https://tc39.es/ecma402/#sec-resolvelocale
 */function ResolveLocale(availableLocales,requestedLocales,options,relevantExtensionKeys,localeData,getDefaultLocale){var matcher=options.localeMatcher;var r;if(matcher==='lookup'){r=LookupMatcher(availableLocales,requestedLocales,getDefaultLocale);}else {r=BestFitMatcher(availableLocales,requestedLocales,getDefaultLocale);}var foundLocale=r.locale;var result={locale:'',dataLocale:foundLocale};var supportedExtension='-u';for(var _i=0,relevantExtensionKeys_1=relevantExtensionKeys;_i<relevantExtensionKeys_1.length;_i++){var key=relevantExtensionKeys_1[_i];invariant(foundLocale in localeData,"Missing locale data for ".concat(foundLocale));var foundLocaleData=localeData[foundLocale];invariant(typeof foundLocaleData==='object'&&foundLocaleData!==null,"locale data ".concat(key," must be an object"));var keyLocaleData=foundLocaleData[key];invariant(Array.isArray(keyLocaleData),"keyLocaleData for ".concat(key," must be an array"));var value=keyLocaleData[0];invariant(typeof value==='string'||value===null,"value must be string or null but got ".concat(typeof value," in key ").concat(key));var supportedExtensionAddition='';if(r.extension){var requestedValue=UnicodeExtensionValue(r.extension,key);if(requestedValue!==undefined){if(requestedValue!==''){if(~keyLocaleData.indexOf(requestedValue)){value=requestedValue;supportedExtensionAddition="-".concat(key,"-").concat(value);}}else if(~requestedValue.indexOf('true')){value='true';supportedExtensionAddition="-".concat(key);}}}if(key in options){var optionsValue=options[key];invariant(typeof optionsValue==='string'||typeof optionsValue==='undefined'||optionsValue===null,'optionsValue must be String, Undefined or Null');if(~keyLocaleData.indexOf(optionsValue)){if(optionsValue!==value){value=optionsValue;supportedExtensionAddition='';}}}result[key]=value;supportedExtension+=supportedExtensionAddition;}if(supportedExtension.length>2){var privateIndex=foundLocale.indexOf('-x-');if(privateIndex===-1){foundLocale=foundLocale+supportedExtension;}else {var preExtension=foundLocale.slice(0,privateIndex);var postExtension=foundLocale.slice(privateIndex,foundLocale.length);foundLocale=preExtension+supportedExtension+postExtension;}foundLocale=Intl.getCanonicalLocales(foundLocale)[0];}result.locale=foundLocale;return result;}

/**
 * https://tc39.es/ecma402/#sec-lookupsupportedlocales
 * @param availableLocales
 * @param requestedLocales
 */function LookupSupportedLocales(availableLocales,requestedLocales){var subset=[];for(var _i=0,requestedLocales_1=requestedLocales;_i<requestedLocales_1.length;_i++){var locale=requestedLocales_1[_i];var noExtensionLocale=locale.replace(UNICODE_EXTENSION_SEQUENCE_REGEX,'');var availableLocale=BestAvailableLocale(availableLocales,noExtensionLocale);if(availableLocale){subset.push(availableLocale);}}return subset;}

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
throw RangeError("Invalid numberingSystems: ".concat(numberingSystem));}opt.nu=numberingSystem;var r=ResolveLocale(availableLocales,requestedLocales,opt,// [[RelevantExtensionKeys]] slot, which is a constant
['nu'],localeData,getDefaultLocale);var dataLocaleData=localeData[r.dataLocale];invariant$1(!!dataLocaleData,"Missing locale data for ".concat(r.dataLocale));var internalSlots=getInternalSlots(nf);internalSlots.locale=r.locale;internalSlots.dataLocale=r.dataLocale;internalSlots.numberingSystem=r.nu;internalSlots.dataLocaleData=dataLocaleData;SetNumberFormatUnitOptions(nf,options,{getInternalSlots:getInternalSlots});var style=internalSlots.style;var mnfdDefault;var mxfdDefault;if(style==='currency'){var currency=internalSlots.currency;var cDigits=CurrencyDigits(currency,{currencyDigitsData:currencyDigitsData});mnfdDefault=cDigits;mxfdDefault=cDigits;}else {mnfdDefault=0;mxfdDefault=style==='percent'?0:3;}var notation=GetOption(options,'notation','string',['standard','scientific','engineering','compact'],'standard');internalSlots.notation=notation;SetNumberFormatDigitOptions(internalSlots,options,mnfdDefault,mxfdDefault,notation);var compactDisplay=GetOption(options,'compactDisplay','string',['short','long'],'short');if(notation==='compact'){internalSlots.compactDisplay=compactDisplay;}var useGrouping=GetOption(options,'useGrouping','boolean',undefined,true);internalSlots.useGrouping=useGrouping;var signDisplay=GetOption(options,'signDisplay','string',['auto','never','always','exceptZero'],'auto');internalSlots.signDisplay=signDisplay;return nf;}

/**
 * https://tc39.es/ecma402/#sec-partitionpattern
 * @param pattern
 */function PartitionPattern(pattern){var result=[];var beginIndex=pattern.indexOf('{');var endIndex=0;var nextIndex=0;var length=pattern.length;while(beginIndex<pattern.length&&beginIndex>-1){endIndex=pattern.indexOf('}',beginIndex);invariant$1(endIndex>beginIndex,"Invalid pattern ".concat(pattern));if(beginIndex>nextIndex){result.push({type:'literal',value:pattern.substring(nextIndex,beginIndex)});}result.push({type:pattern.substring(beginIndex+1,endIndex),value:undefined});nextIndex=endIndex+1;beginIndex=pattern.indexOf('{',nextIndex);}if(nextIndex<length){result.push({type:'literal',value:pattern.substring(nextIndex,length)});}return result;}

/**
 * https://tc39.es/ecma402/#sec-supportedlocales
 * @param availableLocales
 * @param requestedLocales
 * @param options
 */function SupportedLocales(availableLocales,requestedLocales,options){var matcher='best fit';if(options!==undefined){options=ToObject(options);matcher=GetOption(options,'localeMatcher','string',['lookup','best fit'],'best fit');}if(matcher==='best fit'){return LookupSupportedLocales(availableLocales,requestedLocales);}return LookupSupportedLocales(availableLocales,requestedLocales);}

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
    invariant: invariant$1,
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

export { lib as l };
