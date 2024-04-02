import React from "react";
import { PowerBIEmbed } from "powerbi-client-react";
import { models } from "powerbi-client";

function App() {
  return (
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
              "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiJodHRwczovL2FuYWx5c2lzLndpbmRvd3MubmV0L3Bvd2VyYmkvYXBpIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMGEwYWE2M2QtODJkMC00YmExLWI5MDktZDc5ODZlY2U0YzRjLyIsImlhdCI6MTcxMjA0NjUzNSwibmJmIjoxNzEyMDQ2NTM1LCJleHAiOjE3MTIwNTE1MDYsImFjY3QiOjAsImFjciI6IjEiLCJhaW8iOiJBVFFBeS84V0FBQUFLUGdZV05pUlRzZDFhc2hXL1FRMU1SczV2UjZGS1NnOWs5RmV6Ti9ua0xhRzNURUNJaDZXZ3ExTU9ubzBvVStmIiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6Ijg3MWMwMTBmLTVlNjEtNGZiMS04M2FjLTk4NjEwYTdlOTExMCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiSmFpbiIsImdpdmVuX25hbWUiOiJQcmVtIiwiaXBhZGRyIjoiMjQwOTo0MGMyOjExNmQ6ZDNmNTphNTFjOjlkZDI6MjM0MDpkNDFmIiwibmFtZSI6IjIxMTYxX1BSRU1fMjNfMjQiLCJvaWQiOiI2NzVkYjE3NC1hMWE5LTQ2ZmQtYTdiYS0wNWZmN2E1OGRhMzciLCJwdWlkIjoiMTAwMzIwMDI1NURGMDY4NiIsInJoIjoiMC5BWElBUGFZS0N0Q0NvVXU1Q2RlWWJzNU1UQWtBQUFBQUFBQUF3QUFBQUFBQUFBQnlBRUEuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiZVVlUUZXaEE1QnBWemJkNkdzVGJ6eGdGNlVMYnZNRTV2YUhRRVB5VWNZRSIsInRpZCI6IjBhMGFhNjNkLTgyZDAtNGJhMS1iOTA5LWQ3OTg2ZWNlNGM0YyIsInVuaXF1ZV9uYW1lIjoiQzJLMjIxNjhAbXMucGljdC5lZHUiLCJ1cG4iOiJDMksyMjE2OEBtcy5waWN0LmVkdSIsInV0aSI6IjVJZUdGRFZSR1VHcjhtcnVxNjBtQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdfQ.R-jGkBvk37vBU-4HKM6xUqINRpx_QnThy3f9oJd85E_SACTC-Mh0aGKECS31piUjx2oOBA_h72mW7o4S5DPP6y_K-HsOks2hR89ryCRIljXQqJ288rwTTPkKXmt8fvN3p6DWEcZc9C2YlmY7EFJ-mT3mtAP5NdF6qvgbV-IlITeRT1aMPNrpgdYDLlma_KFzvNqJ-khdZnOizRI7APVS2R3MN7ogniXUpVPwjYvekm9tAb7hzwa45ZNiOD0tdv26gVLHz6KTpGxF0LAUzqimhj5WQO_HTVb6n1-K0aK4RwtpARbtm-mlpCwqhXoN493sehtwQFSvxW4DuxC1NvvMqg",
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
  );
}

export default App;
