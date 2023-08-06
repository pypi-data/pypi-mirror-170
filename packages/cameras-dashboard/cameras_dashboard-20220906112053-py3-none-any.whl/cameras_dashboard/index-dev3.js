const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

function toInteger(dirtyNumber){if(dirtyNumber===null||dirtyNumber===true||dirtyNumber===false){return NaN;}var number=Number(dirtyNumber);if(isNaN(number)){return number;}return number<0?Math.ceil(number):Math.floor(number);}

function requiredArgs(required,args){if(args.length<required){throw new TypeError(required+' argument'+(required>1?'s':'')+' required, but only '+args.length+' present');}}

function _typeof(obj){"@babel/helpers - typeof";if(typeof Symbol==="function"&&typeof Symbol.iterator==="symbol"){_typeof=function _typeof(obj){return typeof obj;};}else {_typeof=function _typeof(obj){return obj&&typeof Symbol==="function"&&obj.constructor===Symbol&&obj!==Symbol.prototype?"symbol":typeof obj;};}return _typeof(obj);}/**
 * @name toDate
 * @category Common Helpers
 * @summary Convert the given argument to an instance of Date.
 *
 * @description
 * Convert the given argument to an instance of Date.
 *
 * If the argument is an instance of Date, the function returns its clone.
 *
 * If the argument is a number, it is treated as a timestamp.
 *
 * If the argument is none of the above, the function returns Invalid Date.
 *
 * **Note**: *all* Date arguments passed to any *date-fns* function is processed by `toDate`.
 *
 * @param {Date|Number} argument - the value to convert
 * @returns {Date} the parsed date in the local time zone
 * @throws {TypeError} 1 argument required
 *
 * @example
 * // Clone the date:
 * const result = toDate(new Date(2014, 1, 11, 11, 30, 30))
 * //=> Tue Feb 11 2014 11:30:30
 *
 * @example
 * // Convert the timestamp to date:
 * const result = toDate(1392098430000)
 * //=> Tue Feb 11 2014 11:30:30
 */function toDate(argument){requiredArgs(1,arguments);var argStr=Object.prototype.toString.call(argument);// Clone the date
if(argument instanceof Date||_typeof(argument)==='object'&&argStr==='[object Date]'){// Prevent the date to lose the milliseconds when passed to new Date() in IE10
return new Date(argument.getTime());}else if(typeof argument==='number'||argStr==='[object Number]'){return new Date(argument);}else {if((typeof argument==='string'||argStr==='[object String]')&&typeof console!=='undefined'){// eslint-disable-next-line no-console
console.warn("Starting with v2.0.0-beta.1 date-fns doesn't accept strings as date arguments. Please use `parseISO` to parse strings. See: https://github.com/date-fns/date-fns/blob/master/docs/upgradeGuide.md#string-arguments");// eslint-disable-next-line no-console
console.warn(new Error().stack);}return new Date(NaN);}}

/**
 * @name addMilliseconds
 * @category Millisecond Helpers
 * @summary Add the specified number of milliseconds to the given date.
 *
 * @description
 * Add the specified number of milliseconds to the given date.
 *
 * @param {Date|Number} date - the date to be changed
 * @param {Number} amount - the amount of milliseconds to be added. Positive decimals will be rounded using `Math.floor`, decimals less than zero will be rounded using `Math.ceil`.
 * @returns {Date} the new date with the milliseconds added
 * @throws {TypeError} 2 arguments required
 *
 * @example
 * // Add 750 milliseconds to 10 July 2014 12:45:30.000:
 * const result = addMilliseconds(new Date(2014, 6, 10, 12, 45, 30, 0), 750)
 * //=> Thu Jul 10 2014 12:45:30.750
 */function addMilliseconds(dirtyDate,dirtyAmount){requiredArgs(2,arguments);var timestamp=toDate(dirtyDate).getTime();var amount=toInteger(dirtyAmount);return new Date(timestamp+amount);}

var MILLISECONDS_IN_HOUR=3600000;/**
 * @name addHours
 * @category Hour Helpers
 * @summary Add the specified number of hours to the given date.
 *
 * @description
 * Add the specified number of hours to the given date.
 *
 * @param {Date|Number} date - the date to be changed
 * @param {Number} amount - the amount of hours to be added. Positive decimals will be rounded using `Math.floor`, decimals less than zero will be rounded using `Math.ceil`.
 * @returns {Date} the new date with the hours added
 * @throws {TypeError} 2 arguments required
 *
 * @example
 * // Add 2 hours to 10 July 2014 23:00:00:
 * const result = addHours(new Date(2014, 6, 10, 23, 0), 2)
 * //=> Fri Jul 11 2014 01:00:00
 */function addHours(dirtyDate,dirtyAmount){requiredArgs(2,arguments);var amount=toInteger(dirtyAmount);return addMilliseconds(dirtyDate,amount*MILLISECONDS_IN_HOUR);}

/**
 * Google Chrome as of 67.0.3396.87 introduced timezones with offset that includes seconds.
 * They usually appear for dates that denote time before the timezones were introduced
 * (e.g. for 'Europe/Prague' timezone the offset is GMT+00:57:44 before 1 October 1891
 * and GMT+01:00:00 after that date)
 *
 * Date#getTimezoneOffset returns the offset in minutes and would return 57 for the example above,
 * which would lead to incorrect calculations.
 *
 * This function returns the timezone offset in milliseconds that takes seconds in account.
 */function getTimezoneOffsetInMilliseconds(date){var utcDate=new Date(Date.UTC(date.getFullYear(),date.getMonth(),date.getDate(),date.getHours(),date.getMinutes(),date.getSeconds(),date.getMilliseconds()));utcDate.setUTCFullYear(date.getFullYear());return date.getTime()-utcDate.getTime();}

/**
 * @name startOfDay
 * @category Day Helpers
 * @summary Return the start of a day for the given date.
 *
 * @description
 * Return the start of a day for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @returns {Date} the start of a day
 * @throws {TypeError} 1 argument required
 *
 * @example
 * // The start of a day for 2 September 2014 11:55:00:
 * const result = startOfDay(new Date(2014, 8, 2, 11, 55, 0))
 * //=> Tue Sep 02 2014 00:00:00
 */function startOfDay(dirtyDate){requiredArgs(1,arguments);var date=toDate(dirtyDate);date.setHours(0,0,0,0);return date;}

var MILLISECONDS_IN_DAY=86400000;/**
 * @name differenceInCalendarDays
 * @category Day Helpers
 * @summary Get the number of calendar days between the given dates.
 *
 * @description
 * Get the number of calendar days between the given dates. This means that the times are removed
 * from the dates and then the difference in days is calculated.
 *
 * @param {Date|Number} dateLeft - the later date
 * @param {Date|Number} dateRight - the earlier date
 * @returns {Number} the number of calendar days
 * @throws {TypeError} 2 arguments required
 *
 * @example
 * // How many calendar days are between
 * // 2 July 2011 23:00:00 and 2 July 2012 00:00:00?
 * const result = differenceInCalendarDays(
 *   new Date(2012, 6, 2, 0, 0),
 *   new Date(2011, 6, 2, 23, 0)
 * )
 * //=> 366
 * // How many calendar days are between
 * // 2 July 2011 23:59:00 and 3 July 2011 00:01:00?
 * const result = differenceInCalendarDays(
 *   new Date(2011, 6, 3, 0, 1),
 *   new Date(2011, 6, 2, 23, 59)
 * )
 * //=> 1
 */function differenceInCalendarDays(dirtyDateLeft,dirtyDateRight){requiredArgs(2,arguments);var startOfDayLeft=startOfDay(dirtyDateLeft);var startOfDayRight=startOfDay(dirtyDateRight);var timestampLeft=startOfDayLeft.getTime()-getTimezoneOffsetInMilliseconds(startOfDayLeft);var timestampRight=startOfDayRight.getTime()-getTimezoneOffsetInMilliseconds(startOfDayRight);// Round the number of days to the nearest integer
// because the number of milliseconds in a day is not constant
// (e.g. it's different in the day of the daylight saving time clock shift)
return Math.round((timestampLeft-timestampRight)/MILLISECONDS_IN_DAY);}

// for accurate equality comparisons of UTC timestamps that end up
// having the same representation in local time, e.g. one hour before
// DST ends vs. the instant that DST ends.
function compareLocalAsc(dateLeft,dateRight){var diff=dateLeft.getFullYear()-dateRight.getFullYear()||dateLeft.getMonth()-dateRight.getMonth()||dateLeft.getDate()-dateRight.getDate()||dateLeft.getHours()-dateRight.getHours()||dateLeft.getMinutes()-dateRight.getMinutes()||dateLeft.getSeconds()-dateRight.getSeconds()||dateLeft.getMilliseconds()-dateRight.getMilliseconds();if(diff<0){return -1;}else if(diff>0){return 1;// Return 0 if diff is 0; return NaN if diff is NaN
}else {return diff;}}/**
 * @name differenceInDays
 * @category Day Helpers
 * @summary Get the number of full days between the given dates.
 *
 * @description
 * Get the number of full day periods between two dates. Fractional days are
 * truncated towards zero.
 *
 * One "full day" is the distance between a local time in one day to the same
 * local time on the next or previous day. A full day can sometimes be less than
 * or more than 24 hours if a daylight savings change happens between two dates.
 *
 * To ignore DST and only measure exact 24-hour periods, use this instead:
 * `Math.floor(differenceInHours(dateLeft, dateRight)/24)|0`.
 *
 *
 * @param {Date|Number} dateLeft - the later date
 * @param {Date|Number} dateRight - the earlier date
 * @returns {Number} the number of full days according to the local timezone
 * @throws {TypeError} 2 arguments required
 *
 * @example
 * // How many full days are between
 * // 2 July 2011 23:00:00 and 2 July 2012 00:00:00?
 * const result = differenceInDays(
 *   new Date(2012, 6, 2, 0, 0),
 *   new Date(2011, 6, 2, 23, 0)
 * )
 * //=> 365
 * // How many full days are between
 * // 2 July 2011 23:59:00 and 3 July 2011 00:01:00?
 * const result = differenceInDays(
 *   new Date(2011, 6, 3, 0, 1),
 *   new Date(2011, 6, 2, 23, 59)
 * )
 * //=> 0
 * // How many full days are between
 * // 1 March 2020 0:00 and 1 June 2020 0:00 ?
 * // Note: because local time is used, the
 * // result will always be 92 days, even in
 * // time zones where DST starts and the
 * // period has only 92*24-1 hours.
 * const result = differenceInDays(
 *   new Date(2020, 5, 1),
 *   new Date(2020, 2, 1)
 * )
//=> 92
 */function differenceInDays(dirtyDateLeft,dirtyDateRight){requiredArgs(2,arguments);var dateLeft=toDate(dirtyDateLeft);var dateRight=toDate(dirtyDateRight);var sign=compareLocalAsc(dateLeft,dateRight);var difference=Math.abs(differenceInCalendarDays(dateLeft,dateRight));dateLeft.setDate(dateLeft.getDate()-sign*difference);// Math.abs(diff in full days - diff in calendar days) === 1 if last calendar day is not full
// If so, result must be decreased by 1 in absolute value
var isLastDayNotFull=Number(compareLocalAsc(dateLeft,dateRight)===-sign);var result=sign*(difference-isLastDayNotFull);// Prevent negative zero
return result===0?0:result;}

/**
 * @name endOfDay
 * @category Day Helpers
 * @summary Return the end of a day for the given date.
 *
 * @description
 * Return the end of a day for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @returns {Date} the end of a day
 * @throws {TypeError} 1 argument required
 *
 * @example
 * // The end of a day for 2 September 2014 11:55:00:
 * const result = endOfDay(new Date(2014, 8, 2, 11, 55, 0))
 * //=> Tue Sep 02 2014 23:59:59.999
 */function endOfDay(dirtyDate){requiredArgs(1,arguments);var date=toDate(dirtyDate);date.setHours(23,59,59,999);return date;}

export { addMilliseconds as a, toDate as b, addHours as c, differenceInDays as d, endOfDay as e, requiredArgs as r, startOfDay as s, toInteger as t };
