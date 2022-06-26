

export function validContestName(name){
    if ((name.search(/\d/) !== -1)||
        ( name.toLowerCase().indexOf('изосту')!==-1 )||
        ( name.toLowerCase().indexOf('колл')!==-1 )||
        ( name.toLowerCase().indexOf('клас')!==-1 )||
        ( name.toLowerCase().indexOf('учен')!==-1 )
    ){

        return false
    }
    else {
        return true
    }

}


export function formattingName(name) {
    if (name) {
        let data = name.split(', ')
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
    let authorName = obj.author_name ? `«${obj.author_name.replace(/['"]+/g, '')}», ` : ''
    let material = obj.material ? `${obj.material}, ` : ''
    let age = obj.age ? `${obj.age}, ` : ''
    let fio = obj.fio ? `${formattingName(obj.fio)}, ` : ''
    let school = obj.school ? `${obj.school}, ` : ''
    let fioTeacher = obj.fio_teacher ? `пед. ${obj.fio_teacher}, ` : ''
    let regNumber = obj.reg_number ? `${obj.reg_number}` : ''
    return `${authorName}${material}${age}${fio}${school}${fioTeacher}${regNumber}`

}