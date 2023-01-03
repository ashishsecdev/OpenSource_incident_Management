    <script type="text/javascript">
      (function() {
        var ws = new WebSocket('ws://' + window.location.host + '/jb-server-page?reloadServiceClientId=61');
        ws.onmessage = function (msg) {
          if (msg.data === 'reload') {
            window.location.reload();
          }
          if (msg.data.startsWith('update-css ')) {
            var messageId = msg.data.substring(11);
            var links = document.getElementsByTagName('link');
            for (var i = 0; i < links.length; i++) {
              var link = links[i];
              if (link.rel !== 'stylesheet') continue;
              var clonedLink = link.cloneNode(true);
              var newHref = link.href.replace(/(&|\?)jbUpdateLinksId=\d+/, "$1jbUpdateLinksId=" + messageId);
              if (newHref !== link.href) {
                clonedLink.href = newHref;
              } else {
                var indexOfQuest = newHref.indexOf('?');
                if (indexOfQuest >= 0) {
                  clonedLink.href = newHref.substring(0, indexOfQuest + 1) + 'jbUpdateLinksId=' + messageId + '&' + newHref.substring(indexOfQuest + 1);
                } else {
                  clonedLink.href += '?' + 'jbUpdateLinksId=' + messageId;
                }
              }
              link.replaceWith(clonedLink);
            }
          }
        };
      })();
