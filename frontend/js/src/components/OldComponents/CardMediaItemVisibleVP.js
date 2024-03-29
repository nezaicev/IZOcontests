import {styled} from "@mui/material/styles";
import IconButton from "@mui/material/IconButton";
import * as React from "react";
import Box from "@mui/material/Box";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Collapse from "@mui/material/Collapse";
import CardContent from "@mui/material/CardContent";
import {DividerStyled, ImageListStyled, TypographyStyled} from "../styled";
import ImageGallery from "../Gallary/ImageGallery";
import Typography from "@mui/material//Typography";
import FieldTitle from "../Gallary/FieldTitle";
import {formattingName, validContestName} from "../utils/utils";
import VideoItem from "../Gallary/VideoItem";
import OndemandVideoIcon from "@mui/icons-material/OndemandVideo";
import Tooltip from "@mui/material/Tooltip";
import CameraIcon from '@mui/icons-material/Camera';
import PictureAsPdfIcon from '@mui/icons-material/PictureAsPdf';
import ArticleIcon from '@mui/icons-material/Article';
import ImageList from "@mui/material/ImageList";
import Card from "@mui/material/Card";
import {CardMedia} from "@mui/material";

export const ItemVisibleVP = styled((props) => {
    const {expand, ...other} = props;
    return <IconButton {...other} />;
})(({theme, expand}) => ({
    backgroundColor: 'rgb(239, 236, 227)',
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

            <Card
                sx={{display: 'flex', flexWrap: 'wrap', marginTop: '20px'}}
                name={props.item.author_name} url={props.item.link}
                key={props.reg_number}>
                <CardMedia
                    component="img"
                    sx={{
                        width: 350,
                        display: expanded ? 'none' : 'block',
                        justifyContent: 'center',
                        marginLeft: 'auto',
                        marginRight: 'auto'
                    }}
                    image={props.item.images[0]['md_thumb']}
                    alt={props.item.author_name}
                />

                <Box sx={{
                    flexWrap: "wrap",
                    flexGrow: 1,
                    width: 350
                }}>

                    <CardContent>
                        <Typography component="div" variant="h5"
                                    sx={{
                                        textAlign: 'center',
                                        marginBottom: '25px'
                                    }}>
                            {props.item.author_name}
                        </Typography>
                        <Typography variant="subtitle1" color="text.secondary"
                                    component="div"
                                    sx={{
                                        alignContent: 'center',
                                        display: expanded ? 'none' : 'block',
                                    }}>
                            <FieldTitle title={'№ '}
                                        content={props.item.reg_number}/>
                            <FieldTitle
                                title={props.item.fio.search(',') ||!validContestName(props.item.fio) > 0 ? 'Участники: ' : 'Участник: '}
                                content={validContestName(props.item.fio)?formattingName(props.item.fio):props.item.fio}/>

                            <FieldTitle
                                title={props.item.fio_teacher.search(',') > 0 ? 'Педагоги: ' : 'Педагог: '}
                                content={props.item.fio_teacher}/>

                            <FieldTitle title='Направление: '
                                        content={props.item.direction}/>


                        </Typography>


                    </CardContent>
                </Box>

                <Box sx={{
                    display: 'flex',
                    justifyContent: "right",
                    alignContent: 'flex-end'
                }}>
                    <Box>
                        <ItemVisibleVP
                            expand={expanded}
                            onClick={handleExpandClick}
                            aria-expanded={expanded}
                            aria-label="show more"
                            sx={{p: '5px', marginLeft: '5px'}}
                        >
                            <ExpandMoreIcon/>
                        </ItemVisibleVP>
                    </Box>
                </Box>

            </Card>


            <Collapse in={expanded} timeout="auto" unmountOnExit>
                <Card sx={{marginBottom: '35px'}}>

                    <CardContent>

                        <Box sx={{margin: '20px'}}>

                            <FieldTitle title={'№ '}
                                        content={props.item.reg_number}/>
                            <FieldTitle title={"Регион/город: "}
                                        content={props.item.region + (props.item.city && (props.item.city !== props.item.region) ? ", " + props.item.city : '')}/>
                            <FieldTitle title={'Образовательное уч.: '}
                                        content={props.item.school}/>
                            <FieldTitle title={'Возраст: '}
                                        content={props.item.age}/>

                            <FieldTitle
                                title={props.item.fio.search(',') ||!validContestName(props.item.fio) > 0 ? 'Участники: ' : 'Участник: '}
                                content={validContestName(props.item.fio)?formattingName(props.item.fio):props.item.fio}/>

                            <FieldTitle
                                title={props.item.fio_teacher.search(',') > 0 ? 'Педагоги: ' : 'Педагог: '}
                                content={props.item.fio_teacher}/>


                            <FieldTitle title='Направление: '
                                        content={props.item.direction}/>

                            {
                                props.item.description ?
                                    <Box sx={{marginTop: '10px'}}>
                                        <Typography variant='body2' mt={10}>
                                            {props.item.description}
                                        </Typography> </Box> : ''

                            }

                        </Box>
                        <Box>
                            <Tooltip title="Фото">
                                <IconButton>
                                    <CameraIcon sx={{
                                        fontSize: '2rem',
                                        color: 'rgb(128,110,110)',
                                        padding: '2px'
                                    }}/>
                                </IconButton>
                            </Tooltip>
                            <DividerStyled/>
                        </Box>


                        <ImageGallery images={props.item.images}
                                      titleImg={props.item.author_name}
                                      key={props.index}/>


                        {props.item.videos.length > 0 ?
                            <React.Fragment><Tooltip title="Видео">
                                <IconButton>
                                    <OndemandVideoIcon sx={{
                                        fontSize: '2rem',
                                        color: 'rgb(128,110,110)',
                                        padding: '2px'
                                    }}/>
                                </IconButton>
                            </Tooltip> <DividerStyled/> </React.Fragment> : ''}

                        {
                            props.item.videos.map((item, index) => (
                                <VideoItem name={item.name}
                                           url={item.link}
                                           key={index}/>))

                        }


                        {props.item.files.length > 0 ? <React.Fragment><Tooltip
                            title="Дополнительные материалы">
                            <IconButton>
                                <ArticleIcon sx={{
                                    fontSize: '2rem',
                                    color: 'rgb(128,110,110)',
                                    padding: '2px'
                                }}/>
                            </IconButton>
                        </Tooltip> <DividerStyled/> </React.Fragment> : ''}

                        <Box sx={{
                            marginLeft: 'auto',
                            marginRight: 'auto',
                            display: 'block',
                            width: [250, 500, 1100]
                        }}>

                            {
                                props.item.files.map((item, index) => (


                                    <Box sx={{
                                        display: 'flex',
                                        alignItems: 'center',
                                        marginTop: '10px'
                                    }} key={index}>
                                        <a href={item.link}
                                           download={item.name}>
                                            <IconButton>
                                                <PictureAsPdfIcon sx={{
                                                    fontSize: '2rem',
                                                    color: '#d08686',
                                                    padding: '2px'
                                                }}/>
                                            </IconButton>
                                        </a>
                                        <Typography>
                                            {item.name}
                                        </Typography>
                                    </Box>


                                ))
                            }


                        </Box>

                    </CardContent>
                </Card>
            </Collapse>
        </React.Fragment>
    )


}