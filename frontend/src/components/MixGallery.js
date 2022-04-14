import Card from "@material-ui/core/Card";
import React, {useEffect, useState} from "react";
import {styled} from "@mui/material/styles";
import useInfiniteScroll from "../useInfiniteScroll";
import axios from "axios";
import Box from "@material-ui/core/Box";
import CircularProgress from "@material-ui/core/CircularProgress";
import { ExpandMoreCollapse} from "./ExpandMore";

import ScrollableTabs from "./ScrollableTabs";



const MixCard = styled(Card)(() => ({

    justifyContent: 'center',
    alignItems: 'baseline',
    flexDirection: 'column',
    margin: '20px',
    marginTop: '30px',
    padding: '20px',
    height: 'fit-content',
    boxShadow: 0
}))


export default function MixGallery(props) {


    const [Items, setItems] = useState([]);
    const [isFetching, setIsFetching] = useState(false);

    const [page, setPage] = useState(1);
    const [nomination, setNomination] = useState('');

    const [HasMore, setHasMore] = useState(true);

    const [lastElementRef] = useInfiniteScroll(
        HasMore ? loadMoreItems : () => {
        },
        isFetching
    );

    const resetPage = () => {
        setPage((value) => {
            return 1
        });

    }

    // useEffect(() => {
    //     loadMoreItems();
    // }, []);

    function loadMoreItems() {

        setIsFetching(true);

        axios({
            method: "GET",
            url: `http://${process.env.REACT_APP_HOST_NAME}/frontend/api/archive`,
            params: {
                page_size: 3,
                publish:true,
                contest_name: props.contestName,
                page: page,
                nomination: (nomination === 'Все') ? '' : nomination
            },
        })
            .then((res) => {
                setItems((prevTitles) => {
                    return [...new Set([...prevTitles, ...res.data.results.map((b) => b)])];
                });
                setPage((prevPageNumber) => prevPageNumber + 1);
                setHasMore(!!res.data.next);
                setIsFetching(false);
            })
            .catch((e) => {
                console.log(e);
            });
    }


    return (
        <Box>
            <Box sx={{margin: '20px', width: 'auto'}}>
                <ScrollableTabs url={`http://${process.env.REACT_APP_HOST_NAME}/frontend/api/archive/nominationvp`}
                                loadData={loadMoreItems}
                                resetPage={resetPage}
                                resetLoadedData={() => {
                                    setItems([]);
                                }}
                                setNomination={(value) => {
                                    setNomination(value);

                                }}

                />
            </Box>

            {Items.map((item, index) => {
                if (Items.length === index + 1) {

                    return (
                        <MixCard sx={{boxShadow: '0', padding: '0px'}} key={index}>


                            <ExpandMoreCollapse item={item} lastElementRef={lastElementRef}/>


                        </MixCard>

                    );
                } else {
                    return (<MixCard sx={{boxShadow: '0', padding: '0px'}} key={index}>


                            <ExpandMoreCollapse item={item} index={index}/>


                        </MixCard>

                    )


                }
            })}
            {isFetching && <Box sx={{justifyContent: 'center', height:'600', display:'flex'}}>
                <CircularProgress/>
            </Box>}
        </Box>
    )
}