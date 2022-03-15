import {styled} from "@mui/material/styles";
import IconButton from "@material-ui/core/IconButton";
import * as React from "react";
import Box from "@material-ui/core/Box";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Collapse from "@mui/material/Collapse";
import CardContent from "@material-ui/core/CardContent";
import {DividerStyled, TypographyStyled} from "../styled";
import ImageGallery from "./ImageGallery";
import Typography from "@material-ui/core/Typography";

export const ExpandMore = styled((props) => {
    const {expand, ...other} = props;
    return <IconButton {...other} />;
})(({theme, expand}) => ({
    backgroundColor: 'rgb(239 236 227)',
    '&:hover': {
        backgroundColor: "#c4b7b7",
    },
    margin: '5px',
    display: 'inline-flex',
    transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
        duration: theme.transitions.duration.shortest,
    }),
}));


export function ExpandMoreCollapse(props) {

    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };


    return (<React.Fragment>

            <Box sx={{textAlign: 'center', marginTop: '18px'}} name={props.item.author_name} url={props.item.link}
                 key={props.reg_number}
                 ref={(props.lastElementRef) ? props.lastElementRef : undefined}>
                <Typography variant="h6" gutterBottom
                            component="div">{props.item.author_name} </Typography>
            </Box>


            <Box sx={{display: expanded ? 'none' : 'block'}}>
                <ImageGallery images={props.item.images.slice(0, 3)} titleImg={props.item.author_name}
                              key={props.index}/>

            </Box>
            <Box>
                <ExpandMore
                    expand={expanded}
                    onClick={handleExpandClick}
                    aria-expanded={expanded}
                    aria-label="show more"
                    sx={{p: '5px', marginLeft: '5px'}}
                >
                    <ExpandMoreIcon/>
                </ExpandMore>
            </Box>
            <Collapse in={expanded} timeout="auto" unmountOnExit>
                <CardContent>
                    <DividerStyled/>
                    <Box sx={{margin:'20px'}}>

                            <Typography component={'div'}>
                                № {props.item.reg_number}
                            </Typography>
                            <Typography component={'div'}>
                                Образовательное уч. : {props.item.school}
                            </Typography>
                            <Typography component={'div'}>
                                Участники : {props.item.fio}
                            </Typography>
                            <Typography component={'div'}>
                                Педагог : {props.item.fio_teacher}
                            </Typography >
                            <Typography component={'div'}>
                                {props.item.description}
                            </Typography>


                    </Box>
                    <DividerStyled/>
                    <Box sx={{marginTop: '10px'}}>
                        <ImageGallery images={props.item.images} titleImg={props.item.author_name} key={props.index}/>

                    </Box>

                </CardContent>
            </Collapse>
        </React.Fragment>
    )


}