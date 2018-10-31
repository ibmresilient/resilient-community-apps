# Resilient Integration with Twitter Search API
**This package contains one function which targets the Twitter Search API. Takes in an input of a multiple possible hashtags and a number of Tweets to be returned and contacts the Twitter Search API to return the results. Requires Twitter Access Key and Secret to obtain a OAuth2 read-only token. **
 ![screenshot](./screenshots/1.png)


## app.config settings:
```python
twitter_api_key = <API_KEY>
twitter_api_secret = <API_SECRET>
```

## Function Inputs:
| Function Name | Type | Required | Example |
| ------------- | :--: | :-------:| ------- |
| `twitter_search_tweet_string` | `String` | Yes | `'{"hashtags":[ "Malware"]}'` |
| `twitter_search_tweet_count` | `String` | Yes | `10` |


## Function Output:
```python

results = {
  success = True,
  inputs :{
    twitter_search_tweet_string: <string>,
    twitter_search_tweet_count: <int>
  }
  tweets: {
    statuses: [{
      text: <String>,
      entities: {
          urls:[{
            url : <string>
          }]
        },
        ...OtherAttributes
      }
    }]
  }
}

```
Review the [Twitter API documentation](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html) for more info on all the attributes returned.

The [Twython documentation](https://twython.readthedocs.io/en/latest/) has details specific to the Twython package used by this integration



## Pre-Process Script:
This provided workflow does not utilize the Pre-Processing Script.


## Post-Process Script:
This example **adds a Note to the Incident.**
```python
if (results.success):
  #Prepare the start of the note text
  noteText = u"""<br>Twitter search: 
                Successful : {0}
                <b>Searched Tags:<b>{1}</b>""".format("True" if results["success"] is True else False, results["inputs"]["twitter_search_tweet_string"])
  # For each returned tweet add the text and URL of the tweet to the noteText
  for tweet in results.tweets["statuses"]:
    noteText += u"""<br><br>Tweet Text: <br><b>{0}</b>
    <b>Tweet URL</b> :<a>{1}</a>""".format(tweet["text"],tweet["entities"]["urls"][0]["url"]) 
    
  incident.addNote(helper.createRichText(noteText))
```

## Rules
| Rule Name | Object Type | Workflow Triggered |
| --------- | :---------: | ------------------ |
| Get Popular Tweets For Specified Tag(s) | `Incident` | `Example Twitter: Popular Tweets For Tag(s)` |


To install in "development mode"

    pip install -e ./fn_twitter_most_popular/

After installation, the package will be loaded by `resilient-circuits run`.


To uninstall,

    pip uninstall fn_twitter_most_popular


To package for distribution,

    python ./fn_twitter_most_popular/setup.py sdist

The resulting .tar.gz file can be installed using

    pip install <filename>.tar.gz
