from ..main import split_url



def test_parse():
    splits = ['com', 'aws', 'com.cn']
    test_input = 'apigateway.ca-cent\rral-1.amazonaws.com\rapigateway-fips.ca-centr\ral-1.amazonaws.com.cn\ramplify.us-east-2.amazonaws.com'
    output = 'apigateway.ca-central-1.amazonaws.com\napigateway-fips.ca-central-1.amazonaws.com.cn\namplify.us-east-2.amazonaws.com'

    assert split_url(test_input, splits) == output

def test_parse_no_splits():
    test_input = 'apigateway.ca-cent\rral-1.amazonaws.com\rapigateway-fips.ca-centr\ral-1.amazonaws.com.cn\ramplify.us-east-2.amazonaws.com'
    output = 'apigateway.ca-central-1.amazonaws.comapigateway-fips.ca-central-1.amazonaws.com.cnamplify.us-east-2.amazonaws.com'

    assert split_url(test_input) == output
