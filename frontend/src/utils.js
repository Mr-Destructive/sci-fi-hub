
export let apiUrl = 'http://localhost:8000/graphql/';

export function getCookie(name) {
    var matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ))
    return matches ? decodeURIComponent(matches[1]) : undefined
}

export function setCookie(name, value, props) {
    props = props || {}
    var d = new Date();
    d.setTime(d.getTime() + (7 * 24 * 60 * 60 * 1000));
    var exp = d.toUTCString();
    value = encodeURIComponent(value)
    console.log(exp)
    var updatedCookie = name + "=" + value + "; expires=" + exp + ";Secure;SameSite";
    //for(var propName in props){
    //    if(propName === "HttpOnly" || propName === "Secure" || propName === "SameSite") continue;
    //    updatedCookie += "; " + propName
    //    var propValue = props[propName]
    //    if(propValue !== true){ updatedCookie += "=" + propValue }
    //}
    //if(props.Secure) { updatedCookie += "; Secure" }
    //if(props.SameSite) { updatedCookie += "; SameSite=" + props.SameSite }
    console.log(updatedCookie)
    document.cookie = updatedCookie;
    console.log(document.cookie)
}

export function deleteCookie(name) {
    setCookie(name, null, { expires: -1 })
}
