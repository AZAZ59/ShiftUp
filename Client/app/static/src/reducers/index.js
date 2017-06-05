/**
 * Created by vlad on 18.11.16.
 */
import { combineReducers } from 'redux';

import taskReducer from './task-reducer'

var reducers = combineReducers({
    takReducer: taskReducer
});

export default reducers;