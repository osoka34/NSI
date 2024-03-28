DOXYPYPY_PATH = /Users/alexander/PycharmProjects/tsnm/nsi/bin/doxypypy

gen-doxypypy-docs:
	$(DOXYPYPY_PATH) -a -c internal/controller/http/router.py > internal/controller/http/router.py.out
	$(DOXYPYPY_PATH) -a -c internal/controller/http/v1/graph_algos.py > internal/controller/http/v1/graph_algos.py.out
	$(DOXYPYPY_PATH) -a -c internal/controller/http/v1/health.py > internal/controller/http/v1/health.py.out
	$(DOXYPYPY_PATH) -a -c internal/controller/http/v1/middleware.py > internal/controller/http/v1/middleware.py.out
	$(DOXYPYPY_PATH) -a -c internal/controller/http/v1/nsi.py > internal/controller/http/v1/nsi.py.out

	$(DOXYPYPY_PATH) -a -c internal/app/app.py > internal/app/app.py.out

	$(DOXYPYPY_PATH) -a -c internal/dto/model_graph.py > internal/dto/model_graph.py.out
	$(DOXYPYPY_PATH) -a -c internal/dto/model_nsi.py > internal/dto/model_nsi.py.out

	$(DOXYPYPY_PATH) -a -c internal/entity/repository/model.py > internal/entity/repository/model.py.out
	$(DOXYPYPY_PATH) -a -c internal/entity/repository/repository.py > internal/entity/repository/repository.py.out

	$(DOXYPYPY_PATH) -a -c internal/service/application_graph.py > internal/service/application_graph.py.out
	$(DOXYPYPY_PATH) -a -c internal/service/application_nsi.py > internal/service/application_nsi.py.out

	$(DOXYPYPY_PATH) -a -c internal/usecase/graph_algo/algo_dijkstra.py > internal/usecase/graph_algo/algo_dijkstra.py.out
	$(DOXYPYPY_PATH) -a -c internal/usecase/graph_algo/ant_colony.py > internal/usecase/graph_algo/ant_colony.py.out

	$(DOXYPYPY_PATH) -a -c internal/usecase/parser/parser.py > internal/usecase/parser/parser.py.out

	$(DOXYPYPY_PATH) -a -c internal/usecase/utils/graph_convertor.py > internal/usecase/utils/graph_convertor.py.out
	$(DOXYPYPY_PATH) -a -c internal/usecase/utils/psql_session.py > internal/usecase/utils/psql_session.py.out
	$(DOXYPYPY_PATH) -a -c internal/usecase/utils/validator.py > internal/usecase/utils/validator.py.out

	$(DOXYPYPY_PATH) -a -c main.py > main.py.out

gen-docs:
	doxygen Doxyfile

rm-out:
	find . -type f -name "*.out" -exec rm -f {} \;




.PHONY: gen-docs, gen-doxypypy-docs, rm-out
