import Box from "@mui/material/Box";
import React, {useEffect, useState} from "react";
import useInfiniteScroll from "../hooks/useInfiniteScroll";
import axios from "axios";
import {CardMedia, CircularProgress} from "@mui/material";
import SimpleReactLightbox, {SRLWrapper} from "simple-react-lightbox";
import {optionsSRLWrapper} from "../styled";
import ImageListItem from "@mui/material/ImageListItem";
import Card from "@mui/material/Card";
import {createLabel} from "../utils/utils";


export default function VisibleBoxImages(props) {
    const [items, setItems] = useState([])
    const [isFetching, setIsFetching] = useState(false);
    const [HasMore, setHasMore] = useState(true);


    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );
    useEffect(() => {

        if (props.theme) {
            setItems([])
            props.setPage(1, loadMoreItems())

        }

        if (!props.theme && props.year ) {
            setItems([])
            props.setPage(1, loadMoreItems())

        }



    }, [props.theme, props.year])


    function loadMoreItems() {

        setIsFetching(true);
        axios({
            method: "GET",
            url: props.url,
            params: {
                page_size: 6,
                publish: true,
                contest_name: props.contestName,
                year_contest: props.year,
                page: props.page,
                theme: props.theme,
                ordering: props.ordering ? props.ordering : '-rating',
            },
        })
            .then((res) => {
                setItems((prevTitles) => {
                    return [...new Set([...prevTitles, ...res.data.results.map((b) => b)])];
                });
                props.setPage((prevPageNumber) => prevPageNumber + 1);
                setHasMore(!!res.data.next);
                setIsFetching(false);
            })
            .catch((e) => {
                console.log(e);
            });
    }


    return (
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

                        {items.map((item, index) => (

                            <ImageListItem key={index}
                                           sx={{marginTop: '25px'}}>
                                <Card sx={{border: 7, borderColor: '#fff', boxShadow: 0}}
                                      key={index}
                                      ref={(items.length === index + 1) ? lastElementRef : null}>
                                    <a href={item.image['md_thumb']}>
                                        <img
                                            src={item.image['thumb']}
                                            alt={createLabel(item)}
                                            loading="lazy"
                                        />
                                    </a>
                                </Card>


                            </ImageListItem>))}


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
                    </Box>
                    }

                </SRLWrapper>
            </SimpleReactLightbox>


        </Box>
    )
}

