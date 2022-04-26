

export default function formattingName (name){

    if (name) {
        let data = name.split(', ')
        let result = ''
        data.forEach(function (item, i) {
            result += item.split(' ')[0][0] + '. ' + item.split(' ')[1] + ', '

        })
        return result.slice(0, -2)
    }
    else {
        return ''
    }

}