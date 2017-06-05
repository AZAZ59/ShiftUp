/**
 * Created by vlad on 22.11.16.
 */

var React = require('react');
import {get_result_list} from '../../api/task'
import Result from './result'

class ResultList extends React.Component{
    constructor(props) {
        super(props);
        this.state = {result_list: []};
    }

    componentDidMount() {
        this.update_result_list(this.props.params.result_id);
    }

    update_result_list(){
        get_result_list(this.props.params.result_id).then(data => {
            this.setState({
                result_list: data
            });
        });
    }

    render(){
        return(
            <div>
            <div className="page-header">
                <h2>#{this.props.params.result_id} Результат</h2>
            </div>
                {this.state.result_list ? this.state.result_list.map(function (result) {
                    return(
                        <div>
                            {result.result ? <Result data={JSON.parse(result.result)}/>: ''}
                        </div>
                    )
                }): ''}
            </div>
        );
    }
}

export default ResultList
