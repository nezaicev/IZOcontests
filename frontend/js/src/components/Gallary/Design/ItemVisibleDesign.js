import {styled} from "@mui/material/styles";
import IconButton from "@mui/material/IconButton";
import * as React from "react";
import Box from "@mui/material/Box";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import Collapse from "@mui/material/Collapse";
import CardContent from "@mui/material/CardContent";
import {DividerStyled, ImageListStyled, TypographyStyled} from "../../styled";
import ImageGallery from "../ImageGallery";
import Typography from "@mui/material//Typography";
import FieldTitle from "../FieldTitle";
import {formattingName, validContestName} from "../../utils/utils";
import VideoItem from "../VideoItem";
import OndemandVideoIcon from "@mui/icons-material/OndemandVideo";
import Tooltip from "@mui/material/Tooltip";
import CameraIcon from '@mui/icons-material/Camera';
import PictureAsPdfIcon from '@mui/icons-material/PictureAsPdf';
import ArticleIcon from '@mui/icons-material/Article';
import ImageList from "@mui/material/ImageList";
import Card from "@mui/material/Card";
import {CardMedia} from "@mui/material";
import {ButtonCollapse} from "../../styled";


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

export function ItemVisibleDesign(props) {

    const [expanded, setExpanded] = React.useState(false);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };


    return (<React.Fragment>

            <Card
                sx={{display: 'block', flexWrap: 'wrap', marginTop: '20px'}}
                name={props.item.author_name} url={props.item.link}
                key={props.reg_number}>
                <Box
                    sx={{
                        height: {xs: "auto", sx: 'auto', md: 'auto'},
                        margin: '20px'
                    }}>
                    <Box sx={{
                        display: 'flex',
                        justifyContent: "space-between"
                    }}>
                        <Typography component="div" variant="h5"
                                    sx={{
                                        textAlign: 'center',
                                        marginLeft: '20px'
                                    }}>
                            {props.item.author_name}
                        </Typography>

                        <Box>
                        <ButtonCollapse
                            expand={expanded}
                            onClick={handleExpandClick}
                            aria-expanded={expanded}
                            aria-label="show more"
                            sx={{p: '5px', marginLeft: '5px'}}
                        >
                            <ExpandMoreIcon/>
                        </ButtonCollapse>
                            </Box>

                    </Box>
                    <DividerStyled/>
                    <Box sx={{
                        display: expanded ? 'none' : 'block',
                        textAlign: 'center'
                    }}>
                        <ImageGallery

                            images={props.item.images.slice(0, 3)}
                            titleImg={props.item.author_name}
                            key={props.index}/>


                    </Box>


                </Box>


                <Collapse in={expanded} timeout="auto" unmountOnExit>
                    <Box sx={{marginBottom: '35px'}}>

                        <CardContent>

                            <Box sx={{margin: '20px'}}>

                                <FieldTitle title={"Регион/город: "}
                                            content={props.item.region + (props.item.city && (props.item.city !== props.item.region) ? ", " + props.item.city : '')}/>
                                <FieldTitle title={'Образовательное уч.: '}
                                            content={props.item.school}/>
                                <FieldTitle title={'Возраст: '}
                                            content={props.item.age}/>

                                <FieldTitle
                                    title={props.item.fio.search(',') || !validContestName(props.item.fio) > 0 ? 'Участники: ' : 'Участник: '}
                                    content={validContestName(props.item.fio) ? formattingName(props.item.fio) : props.item.fio}/>

                                <FieldTitle
                                    title={props.item.fio_teacher.search(',') > 0 ? 'Педагоги: ' : 'Педагог: '}
                                    content={props.item.fio_teacher}/>


                                {props.item.direction ? <FieldTitle title='Направление: '
                                            content={props.item.direction}/>:''}

                                {props.item.material ? <FieldTitle title='Техника: '
                                            content={props.item.material}/>:''}

                                {
                                    props.item.description ?
                                        <Box sx={{marginTop: '10px'}}>
                                            <Typography variant='body2'
                                                        mt={10}>
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
                                </Tooltip> <DividerStyled/>
                                </React.Fragment> : ''}

                            {
                                props.item.videos.map((item, index) => (
                                    <VideoItem name={item.name}
                                               url={item.link}
                                               key={index}/>))

                            }


                            {props.item.files.length > 0 ?
                                <React.Fragment><Tooltip
                                    title="Дополнительные материалы">
                                    <IconButton>
                                        <ArticleIcon sx={{
                                            fontSize: '2rem',
                                            color: 'rgb(128,110,110)',
                                            padding: '2px'
                                        }}/>
                                    </IconButton>
                                </Tooltip> <DividerStyled/>
                                </React.Fragment> : ''}

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
                    </Box>
                </Collapse>
            </Card>
        </React.Fragment>
    )


}