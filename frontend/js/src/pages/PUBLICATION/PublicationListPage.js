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
import HorizontalTabs from "../../components/Gallary/HorizontalTabs";

const host = process.env.REACT_APP_HOST_NAME

const PublicationListPage = () => {

    const [page, setPage] = React.useState(1)
    const [years, setYears] = React.useState([]);
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const [data, setData] = React.useState([])
    const [isFetching, setIsFetching] = useState(false);
    const [HasMore, setHasMore] = useState(true);


    function loadMoreItems(dataInitial) {

        setIsFetching(true);
        axios({
            method: "GET",
            url: `${host}/frontend/api/publication/`,
            params: {
                page_size: 3,
                page: page,
                year: dataInitial ? dataInitial[valueHorizontalTabs] : years[valueHorizontalTabs],
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
        setIsFetching(true);
        dataFetch(`${process.env.REACT_APP_HOST_NAME}/frontend/api/publication_years/`, {}, (data) => {
            setYears(data, [function () {
                loadMoreItems(data)
                setIsFetching(false)
            }()])
        })
    }, [])

     useEffect(() => {
        setData([])

        if (years.length > 0) {
            loadMoreItems()
        }

    }, [valueHorizontalTabs])


    return (

        <Container sx={{
            fontFamily: 'Roboto',
            mt: '20px',
            justifyContent: 'center'
        }}>
            <Box sx={{
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'center',
                alignItems: 'center',
                marginBottom: '10px'
            }}>
                <HorizontalTabs
                                data={years}
                                setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue)))}
                />
            </Box>
            <Box sx={{display: 'flex'}}>
                <Grid container spacing={1}
                      sx={{justifyContent: data.length > 2 ? 'space-evenly' : 'flex-start'}}>

                    {data.map((item, index) => (

                        <Grid item xs="auto"
                              key={index} ref={(data.length === index + 1) ? lastElementRef : null}>
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