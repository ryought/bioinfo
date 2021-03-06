#include <stdio.h>
#include <stdlib.h>
#include <glpk.h>


int solve(glp_prob *lp) {
  glp_simplex(lp, NULL);

  switch(glp_get_status(lp)) {
    case GLP_OPT:
      return 0;
      break;
    case GLP_FEAS:
      return -1;
      break;
    default:
      return -2;
      break;
  }
}


int main(void) {
  glp_prob *lp;
  lp = glp_create_prob();

  // read 'data.txt'(CPLEX format problem data)
  glp_read_lp(lp, NULL, "data2.txt");

  // get number of variables
  int num_variables = glp_get_num_cols(lp);
  int A[];

  // solve
  printf("[solved] %d\n", solve(lp));

  printf("opt val = %g\n", glp_get_obj_val(lp));

  printf("[info] %d\n", glp_get_num_rows(lp));

  // column starts from 1
  for(int i=1; i <= glp_get_num_cols(lp); i++) {
    printf("cols[%d] = %g\n", i, glp_get_col_prim(lp, i));
  }

  glp_delete_prob(lp);
  glp_free_env();
  return 0;
}
