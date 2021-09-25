const LOAD_MULTIPLE_STOCKS = 'stocks/LOAD_MULTIPLE_STOCKS';
const LOAD_SINGLE_STOCK = 'stocks/LOAD_SINGLE_STOCK';

const loadManyStocks = stocks => ({
  type: LOAD_MULTIPLE_STOCKS,
  stocks,
});

const loadOneStock = stock => ({
  type: LOAD_SINGLE_STOCK,
  stock,
});

export const getSingleStock = (ticker) => async dispatch => {
  const response = await fetch(`/api/stocks/${ticker}`);

  if (response.ok) {
    const stock = await response.json();
    dispatch(loadOneStock(stock));
  };
};

export const getMultipleStocks = (tickersList) => async dispatch => {
  const stocks = [];
  tickersList.forEach( async ticker => {
    const response = await fetch(`/api/stocks/${ticker}`);

    if (response.ok) {
      const json = await response.json();
      stocks.push(json);
    };
  });
  dispatch(loadManyStocks(stocks));
};

const initialState = {};

export default function stockReducer(state = initialState, action) {
  let newState = {}
  switch (action.type) {
    case LOAD_MULTIPLE_STOCKS:
      const multipleStocks = {};
      action.stocks.forEach(stock => {
        multipleStocks[stock.ticker] = stock;
      });
      return {
        ...multipleStocks,
        ...state,
      };
    case LOAD_SINGLE_STOCK:
      newState = Object.assign({}, state);
      newState[action.stock.ticker] = action.stock;
      return newState;
    default:
      return state;
  }
};
