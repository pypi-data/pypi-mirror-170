const __DEMO__ = false;
    const __SUPERVISOR__ = true;
    const __BUILD__ = "latest"

const documentationUrl=(hass,path)=>`https://store.automacaoraceland.pt/`;// docs - domotica / #${ path } #${
//     hass.config.version.includes("b")
//       ? "rc"
//       : hass.config.version.includes("dev")
//       ? "next"
//       : "www"
//   };
// `https://${
//   hass.config.version.includes("b")
//     ? "rc"
//     : hass.config.version.includes("dev")
//     ? "next"
//     : "www"
// }.home-assistant.io${path}`;

export { documentationUrl as d };
