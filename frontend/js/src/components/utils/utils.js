import dataFetch from "./dataFetch";

const host = process.env.REACT_APP_HOST_NAME


export const years_expositions = (data) => {
    let result = new Set();
    data.forEach((i) => {
        result.add(i['start_date'].split('-')[0])
    });
    return Array.from(result)
}


export function validContestName(name) {
    if ((name.search(/\d/) !== -1) ||
        (name.toLowerCase().indexOf('изосту') !== -1) ||
        (name.toLowerCase().indexOf('колл') !== -1) ||
        (name.toLowerCase().indexOf('клас') !== -1) ||
        (name.toLowerCase().indexOf('учен') !== -1)
    ) {

        return false
    } else {
        return true
    }

}


export function formattingName(name) {
    if (name) {
        const breakpoint = /, +/
        let data = name.split(breakpoint)
        let result = ''
        data.forEach(function (item, i) {
            result += item.split(' ')[0][0] + '. ' + item.split(' ')[1] + ', '
        })
        return result.slice(0, -2)
    } else {
        return ''
    }
}

export function createLabel(obj) {
    const regexp = /[А-Я][А-Яа-яЁё]* [А-Яа-яЁё]\./
    let authorName = obj.author_name ? `«${obj.author_name.replace(/['"]+/g, '')}», ` : ''
    let material = obj.material ? `${obj.material}, ` : ''
    let age = obj.age ? `${obj.age}, ` : ''
    let fio = function () {
        if (obj.fio) {
            if (regexp.test(obj.fio)) {
                return `${obj.fio}, `
            } else {
                return `${formattingName(obj.fio)}, `
            }
        } else {
            return ''
        }


    }()
    let school = obj.school ? `${obj.school}, ` : ''
    let city = obj.city ? `${obj.city}, ` : ''
    let fioTeacher = obj.fio_teacher ? `пед. ${obj.fio_teacher}, ` : ''
    let regNumber = obj.reg_number ? `${obj.reg_number}` : ''
    return `${authorName}${material}${age}${fio}${school}${city}${fioTeacher}${regNumber}`

}

export function getExcludeData(data, exclude) {
    return data.filter((n) => {
        return !exclude.includes(n)
    })
}


export function getFormattedDate(date, options) {

    let newDate = new Date(date)
    return newDate.toLocaleString('ru', options)
}

export function getThumbYoutube(url, quality) {
    let thumbUrl;
    let idVideo = new URL(url)
    idVideo = idVideo.pathname.substr(1, 12).split('&').join('')
    thumbUrl = `http://img.youtube.com/vi/${idVideo}/${quality}.jpg`;
    return thumbUrl
}


export function deleteYoutubeLogo() {
    let logo = document.getElementsByClassName('ytp-impression-link-logo')
    for (let i = 0; i < logo.length; i++) {
        logo[i].outerHTML = "";
    }
    console.log(logo)
}


function stringToColor(string) {
    let hash = 0;
    let i;

    /* eslint-disable no-bitwise */
    for (i = 0; i < string.length; i += 1) {
        hash = string.charCodeAt(i) + ((hash << 5) - hash);
    }

    let color = '#';

    for (i = 0; i < 3; i += 1) {
        const value = (hash >> (i * 8)) & 0xff;
        color += `00${value.toString(16)}`.slice(-2);
    }
    /* eslint-enable no-bitwise */

    return color;
}

export function stringAvatar(name) {
    return {
        sx: {
            backgroundColor: stringToColor(name),
        },
        children: `${name.split('@')[0][0]}`,
    };
}

