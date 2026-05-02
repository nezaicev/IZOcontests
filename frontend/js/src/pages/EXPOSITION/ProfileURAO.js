import Box from "@mui/material/Box";
import {Avatar, CircularProgress, Paper, Typography} from "@mui/material";
import React, {useEffect, useState} from "react";
import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import {optionsSRLWrapper} from "../../components/styled";
import ImageListItem from "@mui/material/ImageListItem";
import Card from "@mui/material/Card";
import {host} from "../../components/utils/consts";
import {useParams, useLocation} from "react-router-dom";
import dataFetch from "../../components/utils/dataFetch";
import Header from "../../components/Header/Header";
import Container from "@mui/material/Container";
import useAuth from "../../components/hooks/useAuth";


function ProfileURAO(props) {
    const auth = useAuth();
    const [fetchAll, setFetchAll] = useState(false);
    const [data, setData] = React.useState({})
    const location = useLocation();
    let {profileId} = useParams()

    useEffect(() => {
        dataFetch(`${host}/urao/api/profiles/${profileId}/`, null, (data) => {
            setData(data);
            setFetchAll(true)
        })
    }, [profileId])

    const pages = [
        {'name': 'УРАО', 'link': '/urao'},
        {'name': 'Студент', 'link': location.pathname},
    ];

    return (
        <Box sx={{fontFamily: 'Roboto', height: 'auto'}}>
            <Header
                pages={pages}
                startPage={1}
                auth={auth}
            />
            <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
                {fetchAll ? <Box>
                    <Box sx={{
                        justifyContent: 'center',
                        display: 'flex',
                        marginTop: '15px',
                        marginBottom: '15px',
                        flexDirection: 'column',
                        alignItems: 'center'
                    }}>
                        <Avatar
                            src={data.avatar_thumb}
                            alt={data.full_name}
                            sx={{width: 150, height: 150, marginBottom: '15px'}}
                        />
                        <Typography variant="h5">
                            {data.full_name}
                        </Typography>
                        {data.year_graduation && (
                            <Typography variant="subtitle1" color="text.secondary" sx={{marginTop: '5px'}}>
                                Год выпуска: {data.year_graduation}
                            </Typography>
                        )}
                    </Box>

                    {/*{data.bio && (*/}
                    {/*    <Paper*/}
                    {/*        sx={{*/}
                    {/*            boxShadow: 0,*/}
                    {/*            overflow: 'auto',*/}
                    {/*            padding: ['5px', '15px'],*/}
                    {/*            marginBottom: '20px'*/}
                    {/*        }}*/}
                    {/*    >*/}
                    {/*        <Typography variant="body1">*/}
                    {/*            {data.bio}*/}
                    {/*        </Typography>*/}
                    {/*    </Paper>*/}
                    {/*)}*/}

                    {data.bio &&(<Paper
                                dangerouslySetInnerHTML={{__html: data.bio}}
                                scroll={'body'}
                                sx={{
                                    boxShadow: 0,
                                    maxHeight: 600,
                                    overflow: 'auto',
                                    padding: ['5px', '15px'],
                                    marginBottom: '20px'
                                }}
                            />)}



                    <Box>
                        <SimpleReactLightbox>
                            <SRLWrapper options={optionsSRLWrapper}>
                                <Box sx={{
                                    display: 'grid',
                                    gridTemplateColumns: `repeat(auto-fill, minmax(320px, 1fr))`,
                                    justifyItems: 'center',
                                    alignItems: 'center',
                                    marginBottom: '30px',
                                }}>

                                    {fetchAll && data.images ? data.images.map((item, index) => (

                                        <ImageListItem key={index}
                                                       sx={{marginTop: '25px'}}>
                                            <Card sx={{
                                                border: 7,
                                                borderColor: '#fff',
                                                boxShadow: 0
                                            }}
                                                  key={index}
                                            >
                                                <a href={item.image_md}>
                                                    <img
                                                        src={item.image_thumb}
                                                        alt={item.author_name}
                                                        loading="lazy"
                                                    />
                                                </a>
                                            </Card>
                                            <Box sx={{
                                                padding: '10px',
                                                textAlign: 'center',
                                                maxWidth: '320px'
                                            }}>
                                                <Typography variant="body2" fontWeight="bold">
                                                    {item.author_name}
                                                </Typography>
                                                <Typography variant="caption" color="text.secondary">
                                                    {item.material_name}, {item.year}
                                                </Typography>
                                                <br/>
                                                <Typography variant="caption" color="text.secondary">
                                                    {item.size} см
                                                </Typography>
                                            </Box>
                                        </ImageListItem>)) : null}
                                </Box>
                            </SRLWrapper>
                        </SimpleReactLightbox>
                    </Box>

                </Box> : <Box sx={{
                    justifyContent: 'center',
                    height: '600',
                    display: 'flex',
                    marginTop: ' 20px'
                }}>
                    <CircularProgress sx={{
                        color: '#d26666'
                    }}/>
                </Box>
                }
            </Container>
        </Box>
    )
}


export default ProfileURAO
