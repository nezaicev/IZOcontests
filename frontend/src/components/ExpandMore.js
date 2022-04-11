import {styled} from "@mui/material/styles";
import IconButton from "@material-ui/core/IconButton";
import * as React from "react";
import Box from "@material-ui/core/Box";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Collapse from "@mui/material/Collapse";
import CardContent from "@material-ui/core/CardContent";
import {DividerStyled, ImageListStyled, TypographyStyled} from "../styled";
import ImageGallery from "./ImageGallery";
import Typography from "@material-ui/core/Typography";
import FieldTitle from "./FieldTitle";
import formattingName from "../utils";
import PlayerModal from "./PlayerModal";
import OndemandVideoIcon from "@mui/icons-material/OndemandVideo";
import Tooltip from "@material-ui/core/Tooltip";
import CameraIcon from '@mui/icons-material/Camera';

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

function createMarkup() {
    return {__html: 'Первый &middot; Второй'};
}


const Root = styled('div')(({theme}) => ({
    width: '100%',
    ...theme.typography.body2,
    '& > :not(style) + :not(style)': {
        marginTop: theme.spacing(2),
    },
}));

export function ExpandMoreCollapse(props) {

    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };


    return (<React.Fragment>

            <Box sx={{textAlign: 'center', marginTop: '18px'}}
                 name={props.item.author_name} url={props.item.link}
                 key={props.reg_number}
                 ref={(props.lastElementRef) ? props.lastElementRef : undefined}>
                <Typography variant="h6" gutterBottom
                            component="div">{props.item.author_name} </Typography>
            </Box>


            <Box sx={{display: expanded ? 'none' : 'block'}}>
                <ImageGallery images={props.item.images.slice(0, 3)}
                              titleImg={props.item.author_name}
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
                    <Box sx={{margin: '20px'}}>

                        <FieldTitle title={'№ '}
                                    content={props.item.reg_number}/>
                        <FieldTitle title={'Образовательное уч.: '}
                                    content={props.item.school}/>
                        <FieldTitle title={'Возраст: '}
                                    content={props.item.age}/>

                        <FieldTitle
                            title={props.item.fio.search(',') > 0 ? 'Участники: ' : 'Участник: '}
                            content={formattingName(props.item.fio)}/>

                        <FieldTitle
                            title={props.item.fio_teacher.search(',') > 0 ? 'Педагоги: ' : 'Педагог: '}
                            content={props.item.fio_teacher}/>

                        <FieldTitle title='Направление: '
                                    content={props.item.direction}/>
                        <FieldTitle title='Описание: '
                                    content={props.item.description}/>

                    </Box>
                    <Box>
                        <Tooltip title="Фото">
                                        <IconButton>
                                            <CameraIcon sx={{ fontSize:'2rem',color: 'rgb(128,110,110)', padding:'2px'}}/>
                                        </IconButton>
                                    </Tooltip>
                        <DividerStyled/>
                    </Box>


                    <Box sx={{
                        marginTop: '10px',
                        marginLeft:'auto',
                        marginRight:'auto',
                        width: [250, 500, 1000]
                    , display:'block',}}>
                        <ImageGallery images={props.item.images}
                                      titleImg={props.item.author_name}
                                      key={props.index}/>

                    </Box>

                    {props.item.videos.length>0 ? <React.Fragment><Tooltip title="Видео">
                                        <IconButton>
                                            <OndemandVideoIcon sx={{ fontSize:'2rem',color: 'rgb(128,110,110)', padding:'2px'}}/>
                                        </IconButton>
                                    </Tooltip> <DividerStyled/> </React.Fragment>:''}
                    <Box sx={{
                        marginLeft:'auto',
                        marginRight:'auto',
                        display:'block',
                        width: [250, 500, 1000]
                    }}>
                        <ImageListStyled sx={{justifyContent: 'space-between'}}
                                         cols={3} rowHeight={250}>
                            {
                                props.item.videos.map((item, index) => (
                                    <PlayerModal name={item.name}
                                                 url={item.link}
                                                 key={index}/>))

                            })
                            }


                        </ImageListStyled>
                    </Box>

                </CardContent>

            </Collapse>
        </React.Fragment>
    )


}