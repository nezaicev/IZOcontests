

$(document).ready(function(){
    $.jMaskGlobals = {
  maskElements: 'input,td,span,div',
  dataMaskAttr: '*[data-mask]',
  dataMask: true,
  watchInterval: 300,
  watchInputs: true,
  watchDataMask: false,
  byPassKeys: [9, 16, 17, 18, 36, 37, 38, 39, 40, 91],
  translation: {
    '0': {pattern: /\d/},
    '9': {pattern: /\d/, optional: true},
    '#': {pattern: /\d/, recursive: true},
    'A': {pattern: /[а-яА-Я0-9]/},
    'S': {pattern: /[а-яА-Я]*/},
    'N': {pattern: /(\s*[1-9])/}
  }
};
  $.applyDataMask();
})