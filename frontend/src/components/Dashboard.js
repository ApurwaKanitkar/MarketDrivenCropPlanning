import React from "react";
import { PowerBIEmbed } from "powerbi-client-react";
import { models } from "powerbi-client";
import Navbar from "./Navbar";

function App() {
  return (
    <>
      <Navbar />
      <div className="App">
        <header className="App-header">
          {/* <img src={logo} className="App-logo" alt="logo" /> */}
          <PowerBIEmbed
            embedConfig={{
              type: "report", // Supported types: report, dashboard, tile, visual and qna
              id: "b04bec28-88b3-4afe-9978-cac4d52f8aac",
              embedUrl:
                "https://app.powerbi.com/reportEmbed?reportId=b04bec28-88b3-4afe-9978-cac4d52f8aac&groupId=e95038cc-8859-49b3-b696-59eed71d784c&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLUlORElBLUNFTlRSQUwtQS1QUklNQVJZLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0IiwiZW1iZWRGZWF0dXJlcyI6eyJ1c2FnZU1ldHJpY3NWTmV4dCI6dHJ1ZSwiZGlzYWJsZUFuZ3VsYXJKU0Jvb3RzdHJhcFJlcG9ydEVtYmVkIjp0cnVlfX0%3d",
              //Update this token in every 1 hr
              accessToken:
                "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMGEwYWE2M2QtODJkMC00YmExLWI5MDktZDc5ODZlY2U0YzRjLyIsImlhdCI6MTcxMjA2NDc1NiwibmJmIjoxNzEyMDY0NzU2LCJleHAiOjE3MTIwNjk4ODIsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVFFBeS84V0FBQUFpZE9IWnk3MGRpUE9Vb0dNQWg4VnltNnRIeG94K3c1aTNRKzlXTlQ3RkVGTnFjV29uZGRSZGl4QVo0dk4rN2JvIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6Ijg3MWMwMTBmLTVlNjEtNGZiMS04M2FjLTk4NjEwYTdlOTExMCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiSmFpbiIsImdpdmVuX25hbWUiOiJQcmVtIiwiaXBhZGRyIjoiMjQwOTo0MGMyOjEwNTU6M2RmYzpiNTZjOmQwMTg6ZjgwMTpmZDMzIiwibmFtZSI6IjIxMTYxX1BSRU1fMjNfMjQiLCJvaWQiOiI2NzVkYjE3NC1hMWE5LTQ2ZmQtYTdiYS0wNWZmN2E1OGRhMzciLCJwdWlkIjoiMTAwMzIwMDI1NURGMDY4NiIsInJoIjoiMC5BWElBUGFZS0N0Q0NvVXU1Q2RlWWJzNU1UQWtBQUFBQUFBQUF3QUFBQUFBQUFBQnlBRUEuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiZVVlUUZXaEE1QnBWemJkNkdzVGJ6eGdGNlVMYnZNRTV2YUhRRVB5VWNZRSIsInRpZCI6IjBhMGFhNjNkLTgyZDAtNGJhMS1iOTA5LWQ3OTg2ZWNlNGM0YyIsInVuaXF1ZV9uYW1lIjoiQzJLMjIxNjhAbXMucGljdC5lZHUiLCJ1cG4iOiJDMksyMjE2OEBtcy5waWN0LmVkdSIsInV0aSI6ImFkQ29zM1JnN2syTWdGSTRrVEE4QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdfQ.h0ndMWpIIC9C-b2PhJAfdhpvfJrROnhbaaVr5oIIj14hskZJpMQWEpRFLxxKYQEIP7YgsSpXQVU3CEoLvkYnsZow1XjaPs-LMlr5GL5y9NU0g0tMer0QmFEj4NliDMbq0vogy81QcoGA-Aa2oxQ0FBVdWSCoT9kUPF6XzFmAww-cRt9rRxNCYkrfShRFsc5U43GcSMQij1pQjZIBIF5SOWBTMrriZ6bTCGNdL5aFT0UI9N3sOysBnCW_3zvhz55yuX0h9GYvUwqc3xTzDG5u9MKS6vBcp61JceGenF6VTCWgGqCKm1ZvPsyN_s4eQpgFIxyp5FX4ggaAqXIQwi1I5g",
              tokenType: models.TokenType.Aad,
              settings: {
                panes: {
                  filters: {
                    expanded: false,
                    visible: true,
                  },
                },
              },
            }}
            eventHandlers={
              new Map([
                [
                  "loaded",
                  function () {
                    console.log("Report loaded");
                  },
                ],
                [
                  "rendered",
                  function () {
                    console.log("Report rendered");
                  },
                ],
                [
                  "error",
                  function (event) {
                    console.log(event.detail);
                  },
                ],
              ])
            }
            cssClassName={"Embed-container"}
            getEmbeddedComponent={(embeddedReport) => {
              window.report = embeddedReport;
            }}
          />
        </header>
      </div>
    </>
  );
}

export default App;
