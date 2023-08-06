const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

import { r as requiredArgs, b as toDate, t as toInteger } from './index-dev3.js';

/**
 * @name addDays
 * @category Day Helpers
 * @summary Add the specified number of days to the given date.
 *
 * @description
 * Add the specified number of days to the given date.
 *
 * @param {Date|Number} date - the date to be changed
 * @param {Number} amount - the amount of days to be added. Positive decimals will be rounded using `Math.floor`, decimals less than zero will be rounded using `Math.ceil`.
 * @returns {Date} - the new date with the days added
 * @throws {TypeError} - 2 arguments required
 *
 * @example
 * // Add 10 days to 1 September 2014:
 * const result = addDays(new Date(2014, 8, 1), 10)
 * //=> Thu Sep 11 2014 00:00:00
 */function addDays(dirtyDate,dirtyAmount){requiredArgs(2,arguments);var date=toDate(dirtyDate);var amount=toInteger(dirtyAmount);if(isNaN(amount)){return new Date(NaN);}if(!amount){// If 0 days, no-op to avoid changing times in the hour before end of DST
return date;}date.setDate(date.getDate()+amount);return date;}

/**
 * @name addMonths
 * @category Month Helpers
 * @summary Add the specified number of months to the given date.
 *
 * @description
 * Add the specified number of months to the given date.
 *
 * @param {Date|Number} date - the date to be changed
 * @param {Number} amount - the amount of months to be added. Positive decimals will be rounded using `Math.floor`, decimals less than zero will be rounded using `Math.ceil`.
 * @returns {Date} the new date with the months added
 * @throws {TypeError} 2 arguments required
 *
 * @example
 * // Add 5 months to 1 September 2014:
 * const result = addMonths(new Date(2014, 8, 1), 5)
 * //=> Sun Feb 01 2015 00:00:00
 */function addMonths(dirtyDate,dirtyAmount){requiredArgs(2,arguments);var date=toDate(dirtyDate);var amount=toInteger(dirtyAmount);if(isNaN(amount)){return new Date(NaN);}if(!amount){// If 0 months, no-op to avoid changing times in the hour before end of DST
return date;}var dayOfMonth=date.getDate();// The JS Date object supports date math by accepting out-of-bounds values for
// month, day, etc. For example, new Date(2020, 0, 0) returns 31 Dec 2019 and
// new Date(2020, 13, 1) returns 1 Feb 2021.  This is *almost* the behavior we
// want except that dates will wrap around the end of a month, meaning that
// new Date(2020, 13, 31) will return 3 Mar 2021 not 28 Feb 2021 as desired. So
// we'll default to the end of the desired month by adding 1 to the desired
// month and using a date of 0 to back up one day to the end of the desired
// month.
var endOfDesiredMonth=new Date(date.getTime());endOfDesiredMonth.setMonth(date.getMonth()+amount+1,0);var daysInMonth=endOfDesiredMonth.getDate();if(dayOfMonth>=daysInMonth){// If we're already at the end of the month, then this is the correct date
// and we're done.
return endOfDesiredMonth;}else {// Otherwise, we now know that setting the original day-of-month value won't
// cause an overflow, so set the desired day-of-month. Note that we can't
// just set the date of `endOfDesiredMonth` because that object may have had
// its time changed in the unusual case where where a DST transition was on
// the last day of the month and its local time was in the hour skipped or
// repeated next to a DST transition.  So we use `date` instead which is
// guaranteed to still have the original time.
date.setFullYear(endOfDesiredMonth.getFullYear(),endOfDesiredMonth.getMonth(),dayOfMonth);return date;}}

var defaultOptions={};function getDefaultOptions(){return defaultOptions;}

/**
 * @name startOfWeek
 * @category Week Helpers
 * @summary Return the start of a week for the given date.
 *
 * @description
 * Return the start of a week for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @param {Object} [options] - an object with options.
 * @param {Locale} [options.locale=defaultLocale] - the locale object. See [Locale]{@link https://date-fns.org/docs/Locale}
 * @param {0|1|2|3|4|5|6} [options.weekStartsOn=0] - the index of the first day of the week (0 - Sunday)
 * @returns {Date} the start of a week
 * @throws {TypeError} 1 argument required
 * @throws {RangeError} `options.weekStartsOn` must be between 0 and 6
 *
 * @example
 * // The start of a week for 2 September 2014 11:55:00:
 * const result = startOfWeek(new Date(2014, 8, 2, 11, 55, 0))
 * //=> Sun Aug 31 2014 00:00:00
 *
 * @example
 * // If the week starts on Monday, the start of the week for 2 September 2014 11:55:00:
 * const result = startOfWeek(new Date(2014, 8, 2, 11, 55, 0), { weekStartsOn: 1 })
 * //=> Mon Sep 01 2014 00:00:00
 */function startOfWeek(dirtyDate,options){var _ref,_ref2,_ref3,_options$weekStartsOn,_options$locale,_options$locale$optio,_defaultOptions$local,_defaultOptions$local2;requiredArgs(1,arguments);var defaultOptions=getDefaultOptions();var weekStartsOn=toInteger((_ref=(_ref2=(_ref3=(_options$weekStartsOn=options===null||options===void 0?void 0:options.weekStartsOn)!==null&&_options$weekStartsOn!==void 0?_options$weekStartsOn:options===null||options===void 0?void 0:(_options$locale=options.locale)===null||_options$locale===void 0?void 0:(_options$locale$optio=_options$locale.options)===null||_options$locale$optio===void 0?void 0:_options$locale$optio.weekStartsOn)!==null&&_ref3!==void 0?_ref3:defaultOptions.weekStartsOn)!==null&&_ref2!==void 0?_ref2:(_defaultOptions$local=defaultOptions.locale)===null||_defaultOptions$local===void 0?void 0:(_defaultOptions$local2=_defaultOptions$local.options)===null||_defaultOptions$local2===void 0?void 0:_defaultOptions$local2.weekStartsOn)!==null&&_ref!==void 0?_ref:0);// Test if weekStartsOn is between 0 and 6 _and_ is not NaN
if(!(weekStartsOn>=0&&weekStartsOn<=6)){throw new RangeError('weekStartsOn must be between 0 and 6 inclusively');}var date=toDate(dirtyDate);var day=date.getDay();var diff=(day<weekStartsOn?7:0)+day-weekStartsOn;date.setDate(date.getDate()-diff);date.setHours(0,0,0,0);return date;}

/**
 * @name addWeeks
 * @category Week Helpers
 * @summary Add the specified number of weeks to the given date.
 *
 * @description
 * Add the specified number of week to the given date.
 *
 * @param {Date|Number} date - the date to be changed
 * @param {Number} amount - the amount of weeks to be added. Positive decimals will be rounded using `Math.floor`, decimals less than zero will be rounded using `Math.ceil`.
 * @returns {Date} the new date with the weeks added
 * @throws {TypeError} 2 arguments required
 *
 * @example
 * // Add 4 weeks to 1 September 2014:
 * const result = addWeeks(new Date(2014, 8, 1), 4)
 * //=> Mon Sep 29 2014 00:00:00
 */function addWeeks(dirtyDate,dirtyAmount){requiredArgs(2,arguments);var amount=toInteger(dirtyAmount);var days=amount*7;return addDays(dirtyDate,days);}

/**
 * @name addYears
 * @category Year Helpers
 * @summary Add the specified number of years to the given date.
 *
 * @description
 * Add the specified number of years to the given date.
 *
 * @param {Date|Number} date - the date to be changed
 * @param {Number} amount - the amount of years to be added. Positive decimals will be rounded using `Math.floor`, decimals less than zero will be rounded using `Math.ceil`.
 * @returns {Date} the new date with the years added
 * @throws {TypeError} 2 arguments required
 *
 * @example
 * // Add 5 years to 1 September 2014:
 * const result = addYears(new Date(2014, 8, 1), 5)
 * //=> Sun Sep 01 2019 00:00:00
 */function addYears(dirtyDate,dirtyAmount){requiredArgs(2,arguments);var amount=toInteger(dirtyAmount);return addMonths(dirtyDate,amount*12);}

/**
 * @name endOfMonth
 * @category Month Helpers
 * @summary Return the end of a month for the given date.
 *
 * @description
 * Return the end of a month for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @returns {Date} the end of a month
 * @throws {TypeError} 1 argument required
 *
 * @example
 * // The end of a month for 2 September 2014 11:55:00:
 * const result = endOfMonth(new Date(2014, 8, 2, 11, 55, 0))
 * //=> Tue Sep 30 2014 23:59:59.999
 */function endOfMonth(dirtyDate){requiredArgs(1,arguments);var date=toDate(dirtyDate);var month=date.getMonth();date.setFullYear(date.getFullYear(),month+1,0);date.setHours(23,59,59,999);return date;}

/**
 * @name startOfMonth
 * @category Month Helpers
 * @summary Return the start of a month for the given date.
 *
 * @description
 * Return the start of a month for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @returns {Date} the start of a month
 * @throws {TypeError} 1 argument required
 *
 * @example
 * // The start of a month for 2 September 2014 11:55:00:
 * const result = startOfMonth(new Date(2014, 8, 2, 11, 55, 0))
 * //=> Mon Sep 01 2014 00:00:00
 */function startOfMonth(dirtyDate){requiredArgs(1,arguments);var date=toDate(dirtyDate);date.setDate(1);date.setHours(0,0,0,0);return date;}

/**
 * @name endOfYear
 * @category Year Helpers
 * @summary Return the end of a year for the given date.
 *
 * @description
 * Return the end of a year for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @returns {Date} the end of a year
 * @throws {TypeError} 1 argument required
 *
 * @example
 * // The end of a year for 2 September 2014 11:55:00:
 * const result = endOfYear(new Date(2014, 8, 2, 11, 55, 00))
 * //=> Wed Dec 31 2014 23:59:59.999
 */function endOfYear(dirtyDate){requiredArgs(1,arguments);var date=toDate(dirtyDate);var year=date.getFullYear();date.setFullYear(year+1,0,0);date.setHours(23,59,59,999);return date;}

/**
 * @name startOfYear
 * @category Year Helpers
 * @summary Return the start of a year for the given date.
 *
 * @description
 * Return the start of a year for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @returns {Date} the start of a year
 * @throws {TypeError} 1 argument required
 *
 * @example
 * // The start of a year for 2 September 2014 11:55:00:
 * const result = startOfYear(new Date(2014, 8, 2, 11, 55, 00))
 * //=> Wed Jan 01 2014 00:00:00
 */function startOfYear(dirtyDate){requiredArgs(1,arguments);var cleanDate=toDate(dirtyDate);var date=new Date(0);date.setFullYear(cleanDate.getFullYear(),0,1);date.setHours(0,0,0,0);return date;}

/**
 * @name endOfWeek
 * @category Week Helpers
 * @summary Return the end of a week for the given date.
 *
 * @description
 * Return the end of a week for the given date.
 * The result will be in the local timezone.
 *
 * @param {Date|Number} date - the original date
 * @param {Object} [options] - an object with options.
 * @param {Locale} [options.locale=defaultLocale] - the locale object. See [Locale]{@link https://date-fns.org/docs/Locale}
 * @param {0|1|2|3|4|5|6} [options.weekStartsOn=0] - the index of the first day of the week (0 - Sunday)
 * @returns {Date} the end of a week
 * @throws {TypeError} 1 argument required
 * @throws {RangeError} `options.weekStartsOn` must be between 0 and 6
 *
 * @example
 * // The end of a week for 2 September 2014 11:55:00:
 * const result = endOfWeek(new Date(2014, 8, 2, 11, 55, 0))
 * //=> Sat Sep 06 2014 23:59:59.999
 *
 * @example
 * // If the week starts on Monday, the end of the week for 2 September 2014 11:55:00:
 * const result = endOfWeek(new Date(2014, 8, 2, 11, 55, 0), { weekStartsOn: 1 })
 * //=> Sun Sep 07 2014 23:59:59.999
 */function endOfWeek(dirtyDate,options){var _ref,_ref2,_ref3,_options$weekStartsOn,_options$locale,_options$locale$optio,_defaultOptions$local,_defaultOptions$local2;requiredArgs(1,arguments);var defaultOptions=getDefaultOptions();var weekStartsOn=toInteger((_ref=(_ref2=(_ref3=(_options$weekStartsOn=options===null||options===void 0?void 0:options.weekStartsOn)!==null&&_options$weekStartsOn!==void 0?_options$weekStartsOn:options===null||options===void 0?void 0:(_options$locale=options.locale)===null||_options$locale===void 0?void 0:(_options$locale$optio=_options$locale.options)===null||_options$locale$optio===void 0?void 0:_options$locale$optio.weekStartsOn)!==null&&_ref3!==void 0?_ref3:defaultOptions.weekStartsOn)!==null&&_ref2!==void 0?_ref2:(_defaultOptions$local=defaultOptions.locale)===null||_defaultOptions$local===void 0?void 0:(_defaultOptions$local2=_defaultOptions$local.options)===null||_defaultOptions$local2===void 0?void 0:_defaultOptions$local2.weekStartsOn)!==null&&_ref!==void 0?_ref:0);// Test if weekStartsOn is between 0 and 6 _and_ is not NaN
if(!(weekStartsOn>=0&&weekStartsOn<=6)){throw new RangeError('weekStartsOn must be between 0 and 6 inclusively');}var date=toDate(dirtyDate);var day=date.getDay();var diff=(day<weekStartsOn?-7:0)+6-(day-weekStartsOn);date.setDate(date.getDate()+diff);date.setHours(23,59,59,999);return date;}

export { addMonths as a, addYears as b, addWeeks as c, addDays as d, endOfMonth as e, startOfMonth as f, startOfWeek as g, endOfYear as h, endOfWeek as i, startOfYear as s };
