import React, {useEffect, useState} from "react";
import Box from "@mui/material/Box";
import axios from "axios";
import useInfiniteScroll from "../../components/hooks/useInfiniteScroll";
import dataFetch from "../../components/utils/dataFetch";
import ImageListItem from "@mui/material/ImageListItem";
import CardExposition from "../../components/Exposition/CardExposition";
import CardPublication from "../../components/Publication/CardPublication";
import {CircularProgress, Grid} from "@mui/material";
import Container from "@mui/material/Container";

const host = process.env.REACT_APP_HOST_NAME

const PublicationListPage = () => {

    const [page, setPage] = React.useState(1)
    const [data, setData] = React.useState([])
    const [isFetching, setIsFetching] = useState(false);
    const [HasMore, setHasMore] = useState(true);


    function loadMoreItems() {

        setIsFetching(true);
        axios({
            method: "GET",
            url: `${host}/frontend/api/publication/`,
            params: {
                page_size: 3,
                page: page,
            },
        })
            .then((res) => {
                setData((prevTitles) => {
                    return [...new Set([...prevTitles, ...res.data.results.map((b) => b)])];
                });
                res.data.next ? setPage((prevPageNumber) => prevPageNumber + 1) : setPage(1);
                setHasMore(!!res.data.next);
                setIsFetching(false);
            })
            .catch((e) => {
                console.log(e);
            });
    }

    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );


    useEffect(() => {
        loadMoreItems()
    }, [])


    return (

         <Container sx={{
                fontFamily: 'Roboto',
                mt: '20px',
                justifyContent: 'center'
            }}>
        <Box sx={{display: 'flex'}}>
            <Grid container spacing={1}
                  sx={{justifyContent: data.length > 2 ? 'space-evenly' : 'flex-start'}}>

                {data.map((item, index) => (

                    <Grid item xs="auto"
                          key={index}  ref={(data.length === index + 1) ? lastElementRef : null}>
                        <CardPublication
                            poster={item.poster} link={item.link} title={item.title}/>
                    </Grid>

                ))}


            </Grid>
        </Box>
               {isFetching && <Box sx={{
                justifyContent: 'center',
                height: '600',
                display: 'flex',
                marginTop: ' 20px'
            }}>
                <CircularProgress sx={{
                    color: '#d26666'
                }}/>
            </Box>}
         </Container>
    )
}

export {PublicationListPage}