#include <stdio.h>
#include <stdlib.h>
#include <glpk.h>

int main(void) {
  glp_prob *lp;
  int ia[1+1000];
  int ja[1+1000];
  double ar[1+1000];
  double z;
  double x1, x2;

  lp = glp_create_prob();
  glp_set_prob_name(lp, "sample");
  glp_set_obj_dir(lp, GLP_MAX);

  glp_add_rows(lp, 3);
  glp_set_row_name(lp, 1, "p");
  glp_set_row_bnds(lp, 1, GLP_UP, 0.0, 4);
  glp_set_row_name(lp, 2, "q");
  glp_set_row_bnds(lp, 2, GLP_UP, 0.0, 12);
  glp_set_row_name(lp, 3, "r");
  glp_set_row_bnds(lp, 3, GLP_UP, 0.0, 1);

  glp_add_cols(lp, 2);
  glp_set_col_name(lp, 1, "x1");
  glp_set_col_bnds(lp, 1, GLP_LO, 0.0, 0.0);
  glp_set_obj_coef(lp, 1, 1);
  glp_set_col_name(lp, 2, "x2");
  glp_set_col_bnds(lp, 2, GLP_LO, 0.0, 0.0);
  glp_set_obj_coef(lp, 2, 1);

  ia[1] = 1, ja[1] = 1, ar[1] = 1.0;
  ia[2] = 1, ja[2] = 2, ar[2] = 2.0;
  ia[3] = 2, ja[3] = 1, ar[3] = 4.0;
  ia[4] = 2, ja[4] = 2, ar[4] = 2.0;
  ia[5] = 3, ja[5] = 1, ar[5] = -1.0;
  ia[6] = 3, ja[6] = 2, ar[6] = 1.0;

  glp_load_matrix(lp, 6, ia, ja, ar);
  glp_simplex(lp, NULL);

  z = glp_get_obj_val(lp);
  x1 = glp_get_col_prim(lp, 1);
  x2 = glp_get_col_prim(lp, 2);
  printf("z = %g, x1 = %g, x2 = %g\n", z, x1, x2);

  glp_delete_prob(lp);
  glp_free_env();
  return 0;
}
