let e=null,o,a,i,s=65,n,c,r=new Set;const d=1111;if(u=document.createElement("link").relList.supports("prefetch")){var u="instantVaryAccept"in document.body.dataset||"Shopify"in window,l=navigator.userAgent.indexOf("Chrome/");if(-1<l&&(e=parseInt(navigator.userAgent.substring(l+"Chrome/".length))),!(u&&e&&e<110)){var h,m,f,l="instantMousedownShortcut"in document.body.dataset,u=(o="instantAllowQueryString"in document.body.dataset,a="instantAllowExternalLinks"in document.body.dataset,i="instantWhitelist"in document.body.dataset,{capture:!0,passive:!0});let t=!1,e=!1,n=!1;if("instantIntensity"in document.body.dataset&&((h=document.body.dataset.instantIntensity).startsWith("mousedown")?(t=!0,"mousedown-only"==h&&(e=!0)):h.startsWith("viewport")?(f=navigator.connection&&navigator.connection.saveData,m=navigator.connection&&navigator.connection.effectiveType&&navigator.connection.effectiveType.includes("2g"),f||m||("viewport"==h?document.documentElement.clientWidth*document.documentElement.clientHeight<45e4&&(n=!0):"viewport-all"==h&&(n=!0))):(f=parseInt(h),isNaN(f)||(s=f))),e||document.addEventListener("touchstart",v,u),t?l||document.addEventListener("mousedown",g,u):document.addEventListener("mouseover",p,u),l&&document.addEventListener("mousedown",y,u),n){let t=window.requestIdleCallback;(t=t||(t=>{t()}))(function(){const e=new IntersectionObserver(t=>{t.forEach(t=>{t.isIntersecting&&(t=t.target,e.unobserve(t),E(t.href))})});document.querySelectorAll("a").forEach(t=>{b(t)&&e.observe(t)})},{timeout:1500})}}}function v(t){n=performance.now();t=t.target.closest("a");b(t)&&E(t.href,"high")}function p(t){if(!(performance.now()-n<d)&&"closest"in t.target){const e=t.target.closest("a");b(e)&&(e.addEventListener("mouseout",w,{passive:!0}),c=setTimeout(()=>{E(e.href,"high"),c=void 0},s))}}function g(t){t=t.target.closest("a");b(t)&&E(t.href,"high")}function w(t){t.relatedTarget&&t.target.closest("a")==t.relatedTarget.closest("a")||c&&(clearTimeout(c),c=void 0)}function y(t){var e;performance.now()-n<d||(e=t.target.closest("a"),1<t.which)||t.metaKey||t.ctrlKey||e&&(e.addEventListener("click",function(t){1337!=t.detail&&t.preventDefault()},{capture:!0,passive:!1,once:!0}),t=new MouseEvent("click",{view:window,bubbles:!0,cancelable:!1,detail:1337}),e.dispatchEvent(t))}function b(t){if(t&&t.href&&(!i||"instant"in t.dataset)){if(t.origin!=location.origin)if(!(a||"instant"in t.dataset)||!e)return;return["http:","https:"].includes(t.protocol)?("http:"!=t.protocol||"https:"!=location.protocol)&&(o||!t.search||"instant"in t.dataset)&&!(t.hash&&t.pathname+t.search==location.pathname+location.search||"noInstant"in t.dataset):void 0}}function E(t,e="auto"){var n;r.has(t)||((n=document.createElement("link")).rel="prefetch",n.href=t,n.fetchPriority=e,n.as="document",document.head.appendChild(n),r.add(t))}
/*

Copyright (C) 2019-2023 Alexandre Dieulot

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*/
