function setStyles() {
    $('#bus').css({'font-family':'sans-serif'});
    
    $('.bus-title').css({'text-align':'center', 
                         'position':'relative', 
                         'top':'10px',
                        'left':'0',
                        'padding':'3px',
                        'margin-left':'10px',
                        'margin-right':'10px',
                        'font-size':'0.9vh',
                        'opacity':'0.7',
                        'border': 'solid 1px rgba(255, 255, 255, 0.3)',
                        'border-radius':'3px'});
    
    $('.bus-info').css({'align-content':'center',
        'display':'block',
        'position':'relative',
        'top':'10px',
        'left':'0',
        'margin-right':'10px',
        'padding':'10px'});
    
    $('.bus-line').css({'display':'inline',
        'margin-right':'10px',
        'font-weight':'bolder',
        'background-color':'#CC3333',
        'padding-left':'30px',
        'padding-right':'30px',
        'float':'left'});
    
    $('.bus-platform').css({
        'display':'inline',
        'margin-right':'2px',
        'background':'#CC3333',
        'border-radius':'10%',
        'padding':'2px 5px 2px 5px'});
    
    $('.bus-platform font').css({'font-size':'15px', 'font-weight':'bold'});
    $('.bus-line img').css({'display':'inline-block', 'margin-right':'2px'});
    $('.bus-arrival').css({'display':'inline'});
    
    $('.bus-exp').css({'display':'inline',
                      'font-size':'80%',
                      'opacity':'0.7',
                      'font-style':'italic',
                      'float':'right'});
}

setStyles();