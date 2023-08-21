import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import {CircularProgress, Grid} from "@mui/material";
import dataFetch from "../../components/utils/dataFetch"
import HorizontalTabs from "../../components/Gallary/HorizontalTabs";
import axios from "axios";
import useInfiniteScroll from "../../components/hooks/useInfiniteScroll";
import VideoItem from "../../components/Video/VideoItem";


let pages = [
    {'name': 'Виде', 'link': 'frontend/api/video/'},
]

const host = process.env.REACT_APP_HOST_NAME

function VideoListPage() {
    const [page, setPage] = React.useState(1)
    const [data, setData] = React.useState([])
    const [categories, setCategories] = React.useState([]);
    const [valueHorizontalTabs, setValueHorizontalTabs] = React.useState(0)
    const [value, setValue] = React.useState(0);
    const [isFetching, setIsFetching] = useState(false);
    const [HasMore, setHasMore] = useState(true);


    function loadMoreItems(dataInitial) {

        setIsFetching(true);
        axios({
            method: "GET",
            url: `${host}/frontend/api/video/`,
            params: {
                page_size: 3,
                category: dataInitial ? dataInitial[valueHorizontalTabs] : categories[valueHorizontalTabs],
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

    useEffect(()=>{setPage(1)}, [categories])


    useEffect(() => {
        setIsFetching(true);
        dataFetch(`${process.env.REACT_APP_HOST_NAME}/frontend/api/video/categories/`, {}, (data) => {
            setCategories(data, [function () {
                loadMoreItems(data)
                setIsFetching(false)
            }()])
        })
    }, [])


    useEffect(() => {
        setData([])

        if (categories.length > 0) {
            loadMoreItems()
        }

    }, [valueHorizontalTabs])


    return (
        <> <Box sx={{
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            alignItems: 'center',
            marginBottom: '10px'
        }}>
            {categories.length > 0 ? <HorizontalTabs
                data={categories}
                setValueHorizontalTabs={(newValue) => (setValueHorizontalTabs((newValue)))}
            /> : ''}
        </Box>

            <Box>
                <Grid container spacing={2}
                      sx={{justifyContent: 'space-between'}}>
                    {data.map((item, index) => (
                        item['link'] ?
                            <Grid item xs="auto" key={index}
                                  ref={(data.length === index + 1) ? lastElementRef : null}>
                                <VideoItem link={item['link']} title={item['title']}
                                           description={item['description']}/>
                            </Grid> : ''
                    ))}

                </Grid>
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
            </Box>


        </>
    )


}

export {VideoListPage}