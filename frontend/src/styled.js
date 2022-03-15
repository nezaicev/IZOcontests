import {styled} from "@mui/material/styles";
import ImageList from "@material-ui/core/ImageList";
import Button from "@material-ui/core/Button";
import {Typography} from "@mui/material";
import ImageListItem from "@material-ui/core/ImageListItem";
import Divider from "@material-ui/core/Divider";


export const DividerStyled=styled(Divider)(()=>({
    backgroundColor:'#efece3',
    height:'2px'
}))
export const ImageListStyled=styled(ImageList)(()=>({
}))

export const TypographyStyled=styled(Typography)(()=>({
    display:"flex",
    fontSize:"0.975rem",
    justifyContent:"center",
    margin: '20px',
    textTransform: 'uppercase'
}))

export const ImageListItemStyled=styled(ImageListItem)(()=>({
    '&:hover': {
        backgroundColor: "#f3e3e3",
    },
    p: '10px',
    backgroundColor: '#ffffff',
    width:'280px',

}))


export const ImageButton = styled(Button)(() => ({
    '&:hover': {
        backgroundColor: "#f3e3e3",
    },
    p: '10px',
    backgroundColor: '#ffffff',


}))